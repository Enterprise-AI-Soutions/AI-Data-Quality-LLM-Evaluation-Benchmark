from src.score_evaluations import (
    calculate_quality_score,
)


WEIGHTS = {
    "accuracy": 0.35,
    "relevance": 0.25,
    "completeness": 0.20,
    "instruction_following": 0.20,
}


def test_perfect_score():
    annotation = {
        "accuracy": 5,
        "relevance": 5,
        "completeness": 5,
        "instruction_following": 5,
    }

    score = calculate_quality_score(
        annotation,
        WEIGHTS,
    )

    assert score == 5.0


def test_weighted_score():
    annotation = {
        "accuracy": 1,
        "relevance": 5,
        "completeness": 5,
        "instruction_following": 5,
    }

    score = calculate_quality_score(
        annotation,
        WEIGHTS,
    )

    assert score == 3.6


def test_low_quality_score():
    annotation = {
        "accuracy": 1,
        "relevance": 1,
        "completeness": 1,
        "instruction_following": 1,
    }

    score = calculate_quality_score(
        annotation,
        WEIGHTS,
    )

    assert score == 1.0
