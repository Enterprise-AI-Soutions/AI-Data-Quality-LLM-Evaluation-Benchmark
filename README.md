# AI Data Quality & LLM Response Evaluation Benchmark

A lightweight Python-based benchmark demonstrating practical
AI response evaluation, annotation quality assurance,
structured-data validation, evaluator agreement analysis,
disagreement detection, and adjudication workflows.

The project is designed as a portfolio demonstration for
AI training, LLM evaluation, AI data quality, annotation QA,
and human-feedback workflows.

---

## Project Objective

AI-generated outputs can appear fluent while containing:

- factual errors;
- unsupported claims;
- hallucinations;
- irrelevant content;
- incomplete responses;
- instruction-following failures;
- structured-output errors.

This project demonstrates a repeatable workflow for
evaluating these issues using explicit rubrics and
structured human annotations.

---

## Scope

The benchmark focuses on three task categories:

### 1. LLM Response Quality

Evaluation of:

- factual accuracy;
- relevance;
- completeness;
- unsupported claims;
- hallucinations.

### 2. Instruction Following

Evaluation of:

- format constraints;
- length constraints;
- required content;
- output-format compliance.

### 3. Structured Output Quality

Evaluation of:

- schema compliance;
- data-type correctness;
- missing required fields.

---

## Architecture

```text
Evaluation Cases
        |
        v
Human Evaluator 1
        |
        +----------------+
                         |
                         v
                  Agreement Analysis
                         ^
                         |
        +----------------+
        |
Human Evaluator 2
        |
        v
Schema Validation
        |
        v
Quality Scoring
        |
        v
Error Analysis
        |
        v
Disagreement Detection
        |
        v
Adjudication Queue
        |
        v
Quality Reports
```

---

## Skills Demonstrated

- AI response evaluation
- LLM evaluation
- AI data quality
- annotation QA
- rubric-based scoring
- hallucination identification
- factuality evaluation
- instruction-following evaluation
- structured-output validation
- JSON and JSONL processing
- Pydantic validation
- Python data processing
- pandas reporting
- evaluator agreement analysis
- disagreement detection
- adjudication workflow
- pytest unit testing

---

## Technology Stack

- Python
- pandas
- Pydantic
- pytest
- JSON
- JSONL
- CSV
- Markdown

No paid API is required.

No model API key is required.

No machine-learning framework is required.

---

## Repository Structure

```text
AI-Data-Quality-LLM-Evaluation-Benchmark/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── pyproject.toml
│
├── data/
│   ├── evaluation_cases.jsonl
│   ├── evaluator_1.jsonl
│   └── evaluator_2.jsonl
│
├── rubrics/
│   └── evaluation_rubric.json
│
├── src/
│   ├── __init__.py
│   ├── schemas.py
│   ├── utils.py
│   ├── validate_data.py
│   ├── score_evaluations.py
│   ├── agreement_analysis.py
│   ├── create_adjudication_queue.py
│   └── generate_report.py
│
├── reports/
│   └── .gitkeep
│
├── tests/
│   ├── __init__.py
│   ├── test_validation.py
│   ├── test_scoring.py
│   └── test_agreement.py
│
├── docs/
│   ├── ANNOTATION_GUIDELINES.md
│   ├── ERROR_TAXONOMY.md
│   └── PROJECT_EXPLANATION.md
│
└── scripts/
    ├── run_pipeline.ps1
    └── run_pipeline.sh
```

---

# Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Data-Quality-LLM-Evaluation-Benchmark.git
```

Move into the repository:

```bash
cd AI-Data-Quality-LLM-Evaluation-Benchmark
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Project Step by Step

## Step 1: Validate Evaluation Cases

```bash
python -m src.validate_data data/evaluation_cases.jsonl --type cases
```

Expected summary:

```text
DATA VALIDATION RESULT
==================================================
File: data/evaluation_cases.jsonl
Total records: 15
Valid records: 15
Validation errors: 0

Validation passed successfully.
```

---

## Step 2: Validate Evaluator 1

```bash
python -m src.validate_data data/evaluator_1.jsonl --type annotations
```

---

## Step 3: Validate Evaluator 2

```bash
python -m src.validate_data data/evaluator_2.jsonl --type annotations
```

---

## Step 4: Score Evaluations

```bash
python -m src.score_evaluations
```

Generated files:

```text
reports/scored_evaluations.jsonl
reports/quality_summary.csv
```

The default quality score is:

```text
Accuracy               35%
Relevance              25%
Completeness           20%
Instruction Following  20%
```

The weights can be changed in:

```text
rubrics/evaluation_rubric.json
```

---

## Step 5: Analyze Evaluator Agreement

```bash
python -m src.agreement_analysis
```

The script calculates:

- exact error-label agreement;
- exact severity agreement;
- disagreement count;
- disagreement rate;
- average score difference by dimension.

Generated output:

```text
reports/agreement_summary.json
```

---

## Step 6: Create Adjudication Queue

```bash
python -m src.create_adjudication_queue
```

Generated output:

```text
reports/disagreement_cases.csv
```

A case is sent for review when:

- primary error labels differ;
- severity labels differ;
- dimension scores differ by two or more points.

The adjudication file contains:

- case ID;
- disagreement reason;
- evaluator 1 error label;
- evaluator 2 error label;
- evaluator severities;
- both written rationales;
- adjudication status;
- final error field;
- final severity field;
- adjudicator rationale field.

---

## Step 7: Generate Evaluation Report

```bash
python -m src.generate_report
```

Generated output:

```text
reports/evaluation_report.md
```

The report contains:

- total evaluations;
- pass/fail summary;
- average quality score;
- error distribution;
- severity distribution;
- evaluator agreement;
- disagreement rate;
- score differences;
- methodology;
- limitations.

---

## Step 8: Run Tests

```bash
pytest -q
```

The tests cover:

- valid evaluation schemas;
- invalid task types;
- valid annotation records;
- score-range validation;
- rationale-length validation;
- weighted scoring;
- exact agreement calculation.

---

# One-Command Execution

## Windows PowerShell

```powershell
.\scripts\run_pipeline.ps1
```

## macOS/Linux

Make the script executable:

```bash
chmod +x scripts/run_pipeline.sh
```

Run:

```bash
./scripts/run_pipeline.sh
```

---

# Annotation Record Example

```json
{
  "case_id": "LLM-001",
  "evaluator_id": "EVAL-001",
  "accuracy": 1,
  "relevance": 5,
  "completeness": 3,
  "instruction_following": 5,
  "primary_error": "factual_error",
  "severity": "major",
  "confidence": 5,
  "rationale": "The response directly answers the question but identifies the wrong city as the capital of Australia."
}
```

---

# Evaluation Workflow

Each response is evaluated independently across four
dimensions.

## Accuracy

Is the response factually and logically correct?

## Relevance

Does it address the actual request?

## Completeness

Does it provide the information necessary to satisfy the
task?

## Instruction Following

Does it follow explicit constraints and requested formats?

---

# Error Taxonomy

The initial taxonomy contains:

- none
- factual_error
- unsupported_claim
- hallucination
- irrelevant
- incomplete
- instruction_violation
- missing_required_content
- format_violation
- schema_error
- missing_required_field

Detailed definitions are available in:

```text
docs/ERROR_TAXONOMY.md
```

---

# Why Evaluator Agreement Matters

Human evaluation contains judgment.

Two evaluators can disagree about:

- the best error category;
- error severity;
- completeness;
- instruction compliance.

The project therefore measures simple, transparent agreement
metrics and routes meaningful disagreements for adjudication.

This repository deliberately uses understandable agreement
statistics rather than adding a machine-learning dependency
for a single metric.

---

# Adjudication Workflow

```text
Evaluator 1 Decision
          |
          +-------------+
                        |
                        v
                 Compare Decisions
                        ^
                        |
          +-------------+
          |
Evaluator 2 Decision
          |
          v
Meaningful Disagreement?
          |
       Yes
          |
          v
Adjudication Queue
          |
          v
Review Prompt + Context
          |
          v
Review Both Rationales
          |
          v
Final Label + Severity
          |
          v
Adjudicator Rationale
```

---

# Portfolio Value

The project demonstrates the ability to:

- evaluate AI-generated outputs;
- apply explicit rubrics;
- write structured evaluation rationales;
- identify hallucinations and factual errors;
- distinguish error categories;
- validate annotation data;
- calculate quality scores;
- analyze evaluator consistency;
- identify disagreements;
- build adjudication workflows;
- generate quality reports.

---

# Suggested CV Description

**AI Data Quality & LLM Response Evaluation Benchmark**

Built a Python-based AI evaluation and annotation QA
workflow covering LLM response quality, instruction
following, and structured JSON outputs. Implemented
rubric-based scoring, hallucination and factuality review,
Pydantic annotation validation, evaluator agreement
analysis, disagreement detection, adjudication queues, and
automated quality reporting.

---

# Suggested Portfolio Description

Designed an end-to-end AI response evaluation workflow for
human annotation and data-quality analysis. The project
validates evaluation records, applies weighted quality
rubrics, analyzes error patterns, measures evaluator
agreement, identifies disagreements, and generates
adjudication queues and quality reports.

---

# Limitations

This is a portfolio-scale synthetic benchmark.

The initial version contains a deliberately small evaluation
dataset intended to demonstrate workflow design and
implementation.

It is not:

- a model leaderboard;
- a comprehensive AI safety benchmark;
- a production evaluation service;
- a replacement for domain-expert review.

Results should not be interpreted as general claims about
the performance of any AI model.

---

# Future Extensions

Potential extensions include:

- 40–60 evaluation cases;
- additional evaluator annotations;
- Hugging Face dataset publishing;
- Label Studio integration;
- local model candidate-response generation;
- RAG factuality evaluation;
- citation correctness evaluation;
- multilingual response evaluation;
- image-description QA as a separate project;
- agent trajectory evaluation as a separate project.

---

# Ethics and Data Quality

The included examples are synthetic and intended for
portfolio demonstration.

Extensions to the repository should avoid:

- confidential customer data;
- private personal information;
- proprietary platform assessment questions;
- unauthorized copyrighted datasets;
- fabricated claims about real paid evaluation work.

Human evaluation is subjective.

Production evaluation systems should document:

- rubric versions;
- evaluator qualifications;
- annotation guidelines;
- disagreement policies;
- adjudication procedures;
- dataset provenance;
- known limitations.

---

# License

The source code is available under the MIT License.
