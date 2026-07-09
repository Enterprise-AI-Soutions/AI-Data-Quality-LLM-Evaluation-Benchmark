#!/usr/bin/env bash

set -e


echo ""
echo "AI Data Quality Evaluation Pipeline"
echo "==================================="


echo ""
echo "Step 1: Validate evaluation cases"

python -m src.validate_data \
data/evaluation_cases.jsonl \
--type cases


echo ""
echo "Step 2: Validate evaluator 1"

python -m src.validate_data \
data/evaluator_1.jsonl \
--type annotations


echo ""
echo "Step 3: Validate evaluator 2"

python -m src.validate_data \
data/evaluator_2.jsonl \
--type annotations


echo ""
echo "Step 4: Score evaluations"

python -m src.score_evaluations


echo ""
echo "Step 5: Analyze evaluator agreement"

python -m src.agreement_analysis


echo ""
echo "Step 6: Create adjudication queue"

python -m src.create_adjudication_queue


echo ""
echo "Step 7: Generate report"

python -m src.generate_report


echo ""
echo "Step 8: Run tests"

pytest -q


echo ""
echo "Pipeline completed successfully."
