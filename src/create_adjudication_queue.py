import argparse
from pathlib import Path

import pandas as pd

from src.agreement_analysis import (
    SCORE_DIMENSIONS,
    analyze_agreement,
)


def identify_disagreement_reasons(
    row: pd.Series,
) -> list[str]:
    """
    Identify reasons a case requires adjudication.
    """

    reasons = []

    if (
        row["primary_error_eval1"]
        !=
        row["primary_error_eval2"]
    ):
        reasons.append(
            "primary_error_label_disagreement"
        )

    if (
        row["severity_eval1"]
        !=
        row["severity_eval2"]
    ):
        reasons.append(
            "severity_disagreement"
        )

    for dimension in SCORE_DIMENSIONS:
        score_gap = abs(
            row[
                f"{dimension}_eval1"
            ]
            -
            row[
                f"{dimension}_eval2"
            ]
        )

        if score_gap >= 2:
            reasons.append(
                f"{dimension}_score_gap"
            )

    return reasons


def create_adjudication_queue(
    evaluator_1_file: str,
    evaluator_2_file: str,
    output_file: str,
) -> pd.DataFrame:
    """
    Create CSV queue for evaluator disagreements.
    """

    _, merged = analyze_agreement(
        evaluator_1_file,
        evaluator_2_file,
    )

    queue_records = []

    for _, row in merged.iterrows():
        reasons = (
            identify_disagreement_reasons(
                row
            )
        )

        if not reasons:
            continue

        queue_records.append(
            {
                "case_id":
                    row["case_id"],

                "disagreement_reasons":
                    "; ".join(reasons),

                "evaluator_1_error":
                    row[
                        "primary_error_eval1"
                    ],

                "evaluator_2_error":
                    row[
                        "primary_error_eval2"
                    ],

                "evaluator_1_severity":
                    row[
                        "severity_eval1"
                    ],

                "evaluator_2_severity":
                    row[
                        "severity_eval2"
                    ],

                "evaluator_1_rationale":
                    row[
                        "rationale_eval1"
                    ],

                "evaluator_2_rationale":
                    row[
                        "rationale_eval2"
                    ],

                "adjudication_status":
                    "pending",

                "final_error_label":
                    "",

                "final_severity":
                    "",

                "adjudicator_rationale":
                    "",
            }
        )

    queue = pd.DataFrame(
        queue_records
    )

    output_path = Path(
        output_file
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    queue.to_csv(
        output_path,
        index=False,
    )

    return queue


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
            "disagreement_cases.csv"
        ),
    )

    args = parser.parse_args()

    queue = create_adjudication_queue(
        args.evaluator_1,
        args.evaluator_2,
        args.output,
    )

    print("\nADJUDICATION QUEUE")
    print("=" * 50)

    print(
        f"Cases requiring review: "
        f"{len(queue)}"
    )

    print(
        f"Output: {args.output}"
    )

    if not queue.empty:
        print("\nCases:")

        print(
            queue[
                [
                    "case_id",
                    "disagreement_reasons",
                ]
            ]
            .to_string(
                index=False
            )
        )


if __name__ == "__main__":
    main()
