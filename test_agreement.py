import pandas as pd

from src.agreement_analysis import (
    calculate_exact_agreement,
)


def test_perfect_agreement():
    evaluator_1 = pd.Series(
        [
            "none",
            "factual_error",
            "irrelevant",
        ]
    )

    evaluator_2 = pd.Series(
        [
            "none",
            "factual_error",
            "irrelevant",
        ]
    )

    agreement = calculate_exact_agreement(
        evaluator_1,
        evaluator_2,
    )

    assert agreement == 1.0


def test_partial_agreement():
    evaluator_1 = pd.Series(
        [
            "none",
            "factual_error",
            "irrelevant",
            "incomplete",
        ]
    )

    evaluator_2 = pd.Series(
        [
            "none",
            "hallucination",
            "irrelevant",
            "incomplete",
        ]
    )

    agreement = calculate_exact_agreement(
        evaluator_1,
        evaluator_2,
    )

    assert agreement == 0.75


def test_zero_agreement():
    evaluator_1 = pd.Series(
        [
            "none",
            "factual_error",
        ]
    )

    evaluator_2 = pd.Series(
        [
            "irrelevant",
            "hallucination",
        ]
    )

    agreement = calculate_exact_agreement(
        evaluator_1,
        evaluator_2,
    )

    assert agreement == 0.0
