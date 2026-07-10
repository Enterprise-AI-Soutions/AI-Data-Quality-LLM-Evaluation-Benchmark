import argparse

from pydantic import ValidationError

from src.schemas import (
    AnnotationRecord,
    EvaluationCase,
)

from src.utils import load_jsonl


def validate_records(
    file_path: str,
    record_type: str,
) -> dict:
    """
    Validate benchmark cases or annotation records.
    """

    records = load_jsonl(file_path)

    errors = []

    valid_count = 0

    seen_keys = set()

    if record_type == "cases":
        schema = EvaluationCase
        unique_fields = ("case_id",)

    elif record_type == "annotations":
        schema = AnnotationRecord
        unique_fields = (
            "case_id",
            "evaluator_id",
        )

    else:
        raise ValueError(
            "record_type must be 'cases' "
            "or 'annotations'"
        )

    for line_number, record in enumerate(
        records,
        start=1,
    ):
        try:
            schema(**record)
            valid_count += 1

        except ValidationError as error:
            errors.append(
                {
                    "line": line_number,
                    "error": str(error),
                }
            )

        unique_key = tuple(
            record.get(field)
            for field in unique_fields
        )

        if unique_key in seen_keys:
            errors.append(
                {
                    "line": line_number,
                    "error": (
                        f"Duplicate record key: "
                        f"{unique_key}"
                    ),
                }
            )

        seen_keys.add(unique_key)

    result = {
        "file": file_path,
        "total_records": len(records),
        "valid_records": valid_count,
        "error_count": len(errors),
        "errors": errors,
    }

    return result


def print_validation_result(
    result: dict,
) -> None:
    """
    Print a readable validation summary.
    """

    print("\nDATA VALIDATION RESULT")
    print("=" * 50)

    print(
        f"File: {result['file']}"
    )

    print(
        f"Total records: "
        f"{result['total_records']}"
    )

    print(
        f"Valid records: "
        f"{result['valid_records']}"
    )

    print(
        f"Validation errors: "
        f"{result['error_count']}"
    )

    if result["errors"]:
        print("\nIssues:")

        for issue in result["errors"]:
            print(
                f"- Line {issue['line']}: "
                f"{issue['error']}"
            )

    else:
        print(
            "\nValidation passed successfully."
        )


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Validate evaluation cases "
            "or annotation records."
        )
    )

    parser.add_argument(
        "file_path",
        help="Path to JSONL file",
    )

    parser.add_argument(
        "--type",
        choices=[
            "cases",
            "annotations",
        ],
        required=True,
        help="Type of records to validate",
    )

    args = parser.parse_args()

    result = validate_records(
        args.file_path,
        args.type,
    )

    print_validation_result(result)

    if result["error_count"] > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
