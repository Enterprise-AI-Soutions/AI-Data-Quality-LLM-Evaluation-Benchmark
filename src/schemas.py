from typing import Any, Literal

from pydantic import BaseModel, Field


TaskType = Literal[
    "llm_response",
    "instruction_following",
    "structured_output",
]


Severity = Literal[
    "none",
    "minor",
    "major",
    "critical",
]


class EvaluationCase(BaseModel):
    case_id: str = Field(min_length=1)

    task_type: TaskType

    category: str = Field(min_length=1)

    prompt: str = Field(min_length=1)

    candidate_response: Any

    reference_context: str = Field(min_length=1)

    expected_primary_error: str = Field(min_length=1)


class AnnotationRecord(BaseModel):
    case_id: str = Field(min_length=1)

    evaluator_id: str = Field(min_length=1)

    accuracy: int = Field(
        ge=1,
        le=5,
    )

    relevance: int = Field(
        ge=1,
        le=5,
    )

    completeness: int = Field(
        ge=1,
        le=5,
    )

    instruction_following: int = Field(
        ge=1,
        le=5,
    )

    primary_error: str = Field(
        min_length=1,
    )

    severity: Severity

    confidence: int = Field(
        ge=1,
        le=5,
    )

    rationale: str = Field(
        min_length=20,
    )
