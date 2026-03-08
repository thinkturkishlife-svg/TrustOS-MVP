"""Trustee matching logic for TrustOS MVP.

This module provides a direct trustee matching function that loads trustee
profiles from SQLite and returns the most compatible options.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from .models import MatchResult, QuestionnaireSubmission


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "trustos.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def _ensure_database_exists() -> None:
    """Create and seed the local SQLite database when it is missing."""
    if DB_PATH.exists():
        return

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def _to_int(value: Any) -> int:
    """Best-effort conversion of trust size inputs to an integer."""
    if isinstance(value, int):
        return value
    if value is None:
        return 0

    cleaned = "".join(ch for ch in str(value) if ch.isdigit())
    return int(cleaned) if cleaned else 0


def _score_compatibility(
    trustee: sqlite3.Row,
    trust_size: int,
    jurisdiction: str,
    needs_directed_trust: bool,
    needs_external_advisor: bool,
) -> float:
    """Compute a compatibility score between 0 and 100."""
    score = 0.0

    # Jurisdiction is a weighted preference: exact match indicates stronger
    # practical compatibility with the requested governing law.
    requested_jurisdiction = (jurisdiction or "").strip().lower()
    trustee_jurisdiction = (trustee["jurisdiction"] or "").strip().lower()
    if requested_jurisdiction and trustee_jurisdiction == requested_jurisdiction:
        score += 40.0

    # Asset fit is treated as a baseline readiness score. Trustees that exceed
    # a user's trust size are excluded before scoring, so this rewards those
    # meeting the minimum qualification.
    if trust_size >= _to_int(trustee["minimum_assets"]):
        score += 15.0

    # Directed-trust support adds value only when explicitly required.
    if needs_directed_trust and bool(trustee["directed_trust_supported"]):
        score += 25.0

    # External-advisor support adds value only when explicitly required.
    if needs_external_advisor and bool(trustee["external_advisor_supported"]):
        score += 20.0

    return round(score, 2)


def match_trustees(
    trust_size: Any,
    jurisdiction: str,
    needs_directed_trust: bool,
    needs_external_advisor: bool,
) -> list[MatchResult]:
    """Return the top five trustees matching user requirements.

    Args:
        trust_size: Estimated trust asset size; supports integers and strings.
        jurisdiction: Requested governing jurisdiction/state.
        needs_directed_trust: Whether directed trust support is required.
        needs_external_advisor: Whether external advisor support is required.

    Returns:
        Up to five ``MatchResult`` entries sorted by descending score.
    """
    _ensure_database_exists()

    parsed_trust_size = _to_int(trust_size)

    query = """
        SELECT trustee_name, minimum_assets, jurisdiction,
               directed_trust_supported, external_advisor_supported
        FROM trustees
    """

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        trustees = conn.execute(
            query,
            (),
        ).fetchall()

    # Hard requirements are exclusionary gates; trustees that fail any required
    # capability or asset threshold are removed before weighted scoring.
    eligible_trustees = [
        trustee
        for trustee in trustees
        if parsed_trust_size >= _to_int(trustee["minimum_assets"])
        and (not needs_directed_trust or bool(trustee["directed_trust_supported"]))
        and (
            not needs_external_advisor
            or bool(trustee["external_advisor_supported"])
        )
    ]

    scored_matches = [
        MatchResult(
            trustee_name=trustee["trustee_name"],
            score=_score_compatibility(
                trustee,
                parsed_trust_size,
                jurisdiction,
                needs_directed_trust,
                needs_external_advisor,
            ),
        )
        for trustee in eligible_trustees
    ]

    return sorted(scored_matches, key=lambda match: match.score or 0.0, reverse=True)[:5]


def find_trustee_matches(submission: QuestionnaireSubmission) -> list[MatchResult]:
    """Bridge questionnaire submissions to the trustee matching engine."""
    return match_trustees(
        trust_size=submission.trust_size,
        jurisdiction=submission.jurisdiction or "",
        needs_directed_trust=bool(getattr(submission, "needs_directed_trust", False)),
        needs_external_advisor=bool(
            getattr(submission, "needs_external_advisor", False)
        ),
    )
