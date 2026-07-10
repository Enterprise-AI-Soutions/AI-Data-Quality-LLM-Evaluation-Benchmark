$ErrorActionPreference = "Stop"

function Run-Step {
    param (
        [string]$Name,
        [scriptblock]$Command
    )

    Write-Host ""
    Write-Host $Name
    Write-Host ""

    & $Command

    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "ERROR: Pipeline failed during: $Name"
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "AI Data Quality Evaluation Pipeline"
Write-Host "==================================="

Run-Step "Step 1: Validate evaluation cases" {
    python -m src.validate_data `
        data/evaluation_cases.jsonl `
        --type cases
}

Run-Step "Step 2: Validate evaluator 1" {
    python -m src.validate_data `
        data/evaluator_1.jsonl `
        --type annotations
}

Run-Step "Step 3: Validate evaluator 2" {
    python -m src.validate_data `
        data/evaluator_2.jsonl `
        --type annotations
}

Run-Step "Step 4: Score evaluations" {
    python -m src.score_evaluations `
        --annotations data/evaluator_1.jsonl `
        --rubric rubrics/evaluation_rubric.json `
        --output-jsonl reports/scored_evaluations.jsonl `
        --output-csv reports/quality_summary.csv
}

Run-Step "Step 5: Analyze evaluator agreement" {
    python -m src.agreement_analysis `
        --evaluator-1 data/evaluator_1.jsonl `
        --evaluator-2 data/evaluator_2.jsonl `
        --output reports/agreement_summary.json
}

Run-Step "Step 6: Create adjudication queue" {
    python -m src.create_adjudication_queue `
        --evaluator-1 data/evaluator_1.jsonl `
        --evaluator-2 data/evaluator_2.jsonl `
        --output reports/disagreement_cases.csv
}

Run-Step "Step 7: Generate report" {
    python -m src.generate_report `
        --scored reports/scored_evaluations.jsonl `
        --agreement reports/agreement_summary.json `
        --output reports/evaluation_report.md
}

Run-Step "Step 8: Run unit tests" {
    python -m pytest -q
}

Write-Host ""
Write-Host "Pipeline completed successfully."