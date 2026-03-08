"""FastAPI entrypoint for the TrustOS MVP backend.

This module will eventually expose API endpoints for:
- health/status checks
- questionnaire submission
- trustee matching results
"""

from fastapi import FastAPI

app = FastAPI(title="TrustOS MVP API")


@app.get("/")
def read_root() -> dict[str, str]:
    """Placeholder root endpoint used to verify the API is running."""
    return {"message": "TrustOS MVP backend scaffold is running."}
