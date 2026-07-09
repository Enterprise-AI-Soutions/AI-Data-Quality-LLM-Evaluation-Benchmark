import argparse
from collections import Counter
from pathlib import Path

import pandas as pd

from src.utils import (
    load_json,
    load_jsonl,
)


def generate_report(
    scored_file: str,
    agreement_file: str,
    output_file: str,
) -> None:
    """
    Generate portfolio-friendly Markdown QA report.
    """

    scored_records = load_jsonl(
        scored_file
    )

    agreement = load_json(
        agreement_file
    )

    dataframe = pd.DataFrame(
        scored_records
    )

    total_cases = len(dataframe)

    passed = int(
        (
            dataframe[
                "quality_status"
            ]
            == "pass"
        ).sum()
    )

    failed = (
        total_cases - passed
    )

    pass_rate = (
        passed / total_cases
        if total_cases
        else 0
    )

    average_score = (
        dataframe[
            "quality_score"
        ].mean()
        if total_cases
        else 0
    )

    error_counts = Counter(
        dataframe[
            "primary_error"
        ]
    )

    severity_counts = Counter(
        dataframe[
            "severity"
        ]
    )

    lines = [
        "# AI Data Quality Evaluation Report",
        "",
        "## Executive Summary",
        "",
        (
            f"- Total evaluations: "
            f"{total_cases}"
        ),
        (
            f"- Passed: {passed}"
        ),
        (
            f"- Failed: {failed}"
        ),
        (
            f"- Pass rate: "
            f"{pass_rate:.1%}"
        ),
        (
            f"- Average quality score: "
            f"{average_score:.2f} / 5.00"
        ),
        "",
        "## Error Distribution",
        "",
    ]

    for error, count in (
        error_counts.most_common()
    ):
        lines.append(
            f"- {error}: {count}"
        )

    lines.extend(
        [
            "",
            "## Severity Distribution",
            "",
        ]
    )

    for severity, count in (
        severity_counts.most_common()
    ):
        lines.append(
            f"- {severity}: {count}"
        )

    lines.extend(
        [
            "",
            "## Evaluator Agreement",
            "",
            (
                f"- Shared cases: "
                f"{agreement['shared_cases']}"
            ),
            (
                f"- Error-label agreement: "
                f"{agreement['error_label_agreement']:.1%}"
            ),
            (
                f"- Severity agreement: "
                f"{agreement['severity_agreement']:.1%}"
            ),
            (
                f"- Disagreement cases: "
                f"{agreement['disagreement_count']}"
            ),
            (
                f"- Disagreement rate: "
                f"{agreement['disagreement_rate']:.1%}"
            ),
            "",
            "## Mean Absolute Score Difference",
            "",
        ]
    )

    for dimension, value in (
        agreement[
            "mean_absolute_score_difference"
        ].items()
    ):
        lines.append(
            f"- {dimension}: {value}"
        )

    lines.extend(
        [
            "",
            "## Evaluation Workflow",
            "",
            (
                "The benchmark applies structured "
                "human evaluation to LLM responses, "
                "instruction-following tasks, and "
                "structured outputs."
            ),
            "",
            (
                "Annotations are validated against "
                "a defined schema, scored using an "
                "explicit rubric, compared across "
                "evaluators, and routed to an "
                "adjudication queue when meaningful "
                "disagreements occur."
            ),
            "",
            "## Limitations",
            "",
            (
                "This is a portfolio-scale synthetic "
                "benchmark intended to demonstrate "
                "AI evaluation and annotation QA "
                "workflow skills."
            ),
            "",
            (
                "The results should not be interpreted "
                "as general model-performance claims."
            ),
        ]
    )

    output_path = Path(
        output_file
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print("\nREPORT GENERATED")
    print("=" * 50)

    print(
        f"Output: {output_path}"
    )


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--scored",
        default=(
            "reports/"
            "scored_evaluations.jsonl"
        ),
    )

    parser.add_argument(
        "--agreement",
        default=(
            "reports/"
            "agreement_summary.json"
        ),
    )

    parser.add_argument(
        "--output",
        default=(
            "reports/"
            "evaluation_report.md"
        ),
    )

    args = parser.parse_args()

    generate_report(
        args.scored,
        args.agreement,
        args.output,
    )


if __name__ == "__main__":
    main()
