import json
from pathlib import Path


def load_jsonl(
    file_path: str | Path,
) -> list[dict]:
    """
    Load a JSONL file and return a list of dictionaries.
    """

    path = Path(file_path)

    records = []

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        for line_number, line in enumerate(
            file,
            start=1,
        ):
            if not line.strip():
                continue

            try:
                record = json.loads(line)

            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON at line "
                    f"{line_number} in {path}"
                ) from error

            records.append(record)

    return records


def load_json(
    file_path: str | Path,
) -> dict:
    """
    Load a standard JSON file.
    """

    path = Path(file_path)

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def write_json(
    data: dict,
    output_path: str | Path,
) -> None:
    """
    Write a dictionary as formatted JSON.
    """

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
        )


def write_jsonl(
    records: list[dict],
    output_path: str | Path,
) -> None:
    """
    Write a list of dictionaries to a JSONL file.
    """

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        for record in records:
            file.write(
                json.dumps(
                    record,
                    ensure_ascii=False,
                )
                + "\n"
            )
