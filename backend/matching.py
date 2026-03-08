"""Trustee matching logic placeholder for TrustOS MVP.

This module will eventually contain business rules and/or scoring logic that
maps questionnaire submissions to recommended trustees.
"""

from .models import MatchResult, QuestionnaireSubmission


def find_trustee_matches(submission: QuestionnaireSubmission) -> list[MatchResult]:
    """Return placeholder results for now.

    Args:
        submission: Questionnaire inputs from the frontend.

    Returns:
        Empty list until matching logic is implemented.
    """
    _ = submission
    return []
