import pytest

from pydantic import ValidationError

from src.schemas import (
    AnnotationRecord,
    EvaluationCase,
)


def test_valid_evaluation_case():
    case = EvaluationCase(
        case_id="TEST-001",
        task_type="llm_response",
        category="accuracy",
        prompt="Test prompt",
        candidate_response="Test response",
        reference_context="Reference context",
        expected_primary_error="none",
    )

    assert case.case_id == "TEST-001"


def test_invalid_task_type():
    with pytest.raises(
        ValidationError
    ):
        EvaluationCase(
            case_id="TEST-001",
            task_type="unknown_type",
            category="accuracy",
            prompt="Test prompt",
            candidate_response="Test response",
            reference_context="Reference context",
            expected_primary_error="none",
        )


def test_valid_annotation():
    annotation = AnnotationRecord(
        case_id="TEST-001",
        evaluator_id="EVAL-001",
        accuracy=5,
        relevance=5,
        completeness=4,
        instruction_following=5,
        primary_error="none",
        severity="none",
        confidence=5,
        rationale=(
            "The response is correct and "
            "fully addresses the requested task."
        ),
    )

    assert annotation.accuracy == 5


def test_invalid_annotation_score():
    with pytest.raises(
        ValidationError
    ):
        AnnotationRecord(
            case_id="TEST-001",
            evaluator_id="EVAL-001",
            accuracy=7,
            relevance=5,
            completeness=4,
            instruction_following=5,
            primary_error="none",
            severity="none",
            confidence=5,
            rationale=(
                "The response is correct and "
                "fully addresses the task."
            ),
        )


def test_short_rationale_rejected():
    with pytest.raises(
        ValidationError
    ):
        AnnotationRecord(
            case_id="TEST-001",
            evaluator_id="EVAL-001",
            accuracy=5,
            relevance=5,
            completeness=5,
            instruction_following=5,
            primary_error="none",
            severity="none",
            confidence=5,
            rationale="Looks good.",
        )
