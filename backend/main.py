"""FastAPI entrypoint for the TrustOS MVP backend.

This module will eventually expose API endpoints for:
- health/status checks
- questionnaire submission
- trustee matching results
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .matching import match_trustees
from .models import MatchRequest, MatchResult

app = FastAPI(title="TrustOS MVP API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root() -> dict[str, str]:
    """Placeholder root endpoint used to verify the API is running."""
    return {"message": "TrustOS MVP backend scaffold is running."}


@app.post("/match", response_model=list[MatchResult])
def match(payload: MatchRequest) -> list[MatchResult]:
    """Return top trustee matches for explicit matching criteria."""
    return match_trustees(
        trust_size=payload.trust_size,
        jurisdiction=payload.jurisdiction,
        needs_directed_trust=payload.needs_directed_trust,
        needs_external_advisor=payload.needs_external_advisor,
    )
