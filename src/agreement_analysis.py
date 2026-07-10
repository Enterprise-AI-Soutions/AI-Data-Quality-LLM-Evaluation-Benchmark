import argparse

import pandas as pd

from src.utils import (
    load_jsonl,
    write_json,
)


SCORE_DIMENSIONS = [
    "accuracy",
    "relevance",
    "completeness",
    "instruction_following",
]


def calculate_exact_agreement(
    series_1: pd.Series,
    series_2: pd.Series,
) -> float:
    """
    Calculate exact agreement proportion.
    """

    if len(series_1) == 0:
        return 0.0

    agreement = (
        series_1 == series_2
    ).mean()

    return round(
        float(agreement),
        3,
    )


def analyze_agreement(
    evaluator_1_file: str,
    evaluator_2_file: str,
) -> tuple[dict, pd.DataFrame]:
    """
    Compare two evaluator annotation files.
    """

    evaluator_1 = pd.DataFrame(
        load_jsonl(
            evaluator_1_file
        )
    )

    evaluator_2 = pd.DataFrame(
        load_jsonl(
            evaluator_2_file
        )
    )

    merged = evaluator_1.merge(
        evaluator_2,
        on="case_id",
        suffixes=(
            "_eval1",
            "_eval2",
        ),
    )

    if merged.empty:
        raise ValueError(
            "No shared case IDs were found."
        )

    error_agreement = (
        calculate_exact_agreement(
            merged[
                "primary_error_eval1"
            ],
            merged[
                "primary_error_eval2"
            ],
        )
    )

    severity_agreement = (
        calculate_exact_agreement(
            merged[
                "severity_eval1"
            ],
            merged[
                "severity_eval2"
            ],
        )
    )

    score_differences = {}

    for dimension in SCORE_DIMENSIONS:
        difference = (
            merged[
                f"{dimension}_eval1"
            ]
            -
            merged[
                f"{dimension}_eval2"
            ]
        ).abs()

        score_differences[
            dimension
        ] = round(
            float(
                difference.mean()
            ),
            3,
        )

    disagreement_mask = (
        (
            merged[
                "primary_error_eval1"
            ]
            !=
            merged[
                "primary_error_eval2"
            ]
        )
        |
        (
            merged[
                "severity_eval1"
            ]
            !=
            merged[
                "severity_eval2"
            ]
        )
    )

    disagreement_count = int(
        disagreement_mask.sum()
    )

    disagreement_rate = round(
        disagreement_count
        / len(merged),
        3,
    )

    report = {
        "shared_cases": len(merged),

        "error_label_agreement":
            error_agreement,

        "severity_agreement":
            severity_agreement,

        "disagreement_count":
            disagreement_count,

        "disagreement_rate":
            disagreement_rate,

        "mean_absolute_score_difference":
            score_differences,
    }

    return report, merged


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--evaluator-1",
        default=(
            "data/evaluator_1.jsonl"
        ),
    )

    parser.add_argument(
        "--evaluator-2",
        default=(
            "data/evaluator_2.jsonl"
        ),
    )

    parser.add_argument(
        "--output",
        default=(
            "reports/"
            "agreement_summary.json"
        ),
    )

    args = parser.parse_args()

    report, _ = analyze_agreement(
        args.evaluator_1,
        args.evaluator_2,
    )

    write_json(
        report,
        args.output,
    )

    print("\nEVALUATOR AGREEMENT SUMMARY")
    print("=" * 50)

    print(
        f"Shared cases: "
        f"{report['shared_cases']}"
    )

    print(
        f"Error-label agreement: "
        f"{report['error_label_agreement']:.1%}"
    )

    print(
        f"Severity agreement: "
        f"{report['severity_agreement']:.1%}"
    )

    print(
        f"Disagreement cases: "
        f"{report['disagreement_count']}"
    )

    print(
        f"Disagreement rate: "
        f"{report['disagreement_rate']:.1%}"
    )

    print(
        "\nMean absolute score differences:"
    )

    for dimension, difference in (
        report[
            "mean_absolute_score_difference"
        ].items()
    ):
        print(
            f"- {dimension}: {difference}"
        )


if __name__ == "__main__":
    main()
