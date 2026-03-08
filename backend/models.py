"""Data model placeholders for the TrustOS MVP backend.

In future iterations, this file can include:
- Pydantic request/response schemas for FastAPI
- SQLite persistence models (e.g., via SQLAlchemy or SQLModel)
"""

from pydantic import BaseModel


class MatchRequest(BaseModel):
    """Input schema for direct trustee matching requests."""

    trust_size: int | float
    jurisdiction: str
    needs_directed_trust: bool
    needs_external_advisor: bool


class QuestionnaireSubmission(BaseModel):
    """Placeholder schema for questionnaire input data."""

    # TODO: Add concrete questionnaire fields.
    trust_size: str | None = None
    jurisdiction: str | None = None


class MatchResult(BaseModel):
    """Placeholder schema for trustee match output."""

    # TODO: Add concrete match result fields.
    trustee_name: str | None = None
    score: float | None = None
