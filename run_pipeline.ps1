Write-Host ""
Write-Host "AI Data Quality Evaluation Pipeline"
Write-Host "==================================="


Write-Host ""
Write-Host "Step 1: Validate evaluation cases"

python -m src.validate_data `
data/evaluation_cases.jsonl `
--type cases


Write-Host ""
Write-Host "Step 2: Validate evaluator 1"

python -m src.validate_data `
data/evaluator_1.jsonl `
--type annotations


Write-Host ""
Write-Host "Step 3: Validate evaluator 2"

python -m src.validate_data `
data/evaluator_2.jsonl `
--type annotations


Write-Host ""
Write-Host "Step 4: Score evaluations"

python -m src.score_evaluations


Write-Host ""
Write-Host "Step 5: Analyze evaluator agreement"

python -m src.agreement_analysis


Write-Host ""
Write-Host "Step 6: Create adjudication queue"

python -m src.create_adjudication_queue


Write-Host ""
Write-Host "Step 7: Generate report"

python -m src.generate_report


Write-Host ""
Write-Host "Step 8: Run unit tests"

pytest -q


Write-Host ""
Write-Host "Pipeline completed successfully."
