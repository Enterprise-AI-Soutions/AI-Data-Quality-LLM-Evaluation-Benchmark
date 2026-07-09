import argparse
from pathlib import Path

import pandas as pd

from src.utils import (
    load_json,
    load_jsonl,
    write_jsonl,
)


def calculate_quality_score(
    annotation: dict,
    weights: dict,
) -> float:
    """
    Calculate weighted quality score.
    """

    score = 0.0

    for dimension, weight in weights.items():
        score += (
            annotation[dimension]
            * weight
        )

    return round(score, 2)


def score_evaluations(
    annotation_file: str,
    rubric_file: str,
    output_jsonl: str,
    output_csv: str,
) -> list[dict]:
    """
    Calculate scores and quality status for annotations.
    """

    annotations = load_jsonl(
        annotation_file
    )

    rubric = load_json(
        rubric_file
    )

    weights = {
        dimension: settings["weight"]
        for dimension, settings
        in rubric["dimensions"].items()
    }

    threshold = rubric[
        "pass_threshold"
    ]

    scored_records = []

    for annotation in annotations:
        quality_score = (
            calculate_quality_score(
                annotation,
                weights,
            )
        )

        scored_record = {
            **annotation,
            "quality_score": quality_score,
            "quality_status": (
                "pass"
                if quality_score >= threshold
                else "fail"
            ),
        }

        scored_records.append(
            scored_record
        )

    write_jsonl(
        scored_records,
        output_jsonl,
    )

    output_path = Path(output_csv)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataframe = pd.DataFrame(
        scored_records
    )

    dataframe.to_csv(
        output_path,
        index=False,
    )

    return scored_records


def print_summary(
    scored_records: list[dict],
) -> None:
    """
    Print score summary.
    """

    dataframe = pd.DataFrame(
        scored_records
    )

    print("\nQUALITY SCORING SUMMARY")
    print("=" * 50)

    print(
        f"Total evaluations: "
        f"{len(dataframe)}"
    )

    print(
        f"Average quality score: "
        f"{dataframe['quality_score'].mean():.2f}"
    )

    print(
        "\nQuality status:"
    )

    print(
        dataframe[
            "quality_status"
        ]
        .value_counts()
        .to_string()
    )

    print(
        "\nPrimary error distribution:"
    )

    print(
        dataframe[
            "primary_error"
        ]
        .value_counts()
        .to_string()
    )


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--annotations",
        default="data/evaluator_1.jsonl",
    )

    parser.add_argument(
        "--rubric",
        default=(
            "rubrics/"
            "evaluation_rubric.json"
        ),
    )

    parser.add_argument(
        "--output-jsonl",
        default=(
            "reports/"
            "scored_evaluations.jsonl"
        ),
    )

    parser.add_argument(
        "--output-csv",
        default=(
            "reports/"
            "quality_summary.csv"
        ),
    )

    args = parser.parse_args()

    records = score_evaluations(
        args.annotations,
        args.rubric,
        args.output_jsonl,
        args.output_csv,
    )

    print_summary(records)


if __name__ == "__main__":
    main()
