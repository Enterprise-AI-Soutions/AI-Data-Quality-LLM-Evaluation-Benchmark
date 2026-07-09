# Project Explanation

## Business Problem

AI-generated outputs can be fluent while still being:

- factually wrong;
- unsupported by evidence;
- incomplete;
- irrelevant;
- inconsistent with instructions;
- structurally invalid.

Organizations using AI systems need repeatable evaluation
processes to identify these issues.

---

## Project Objective

This project demonstrates a lightweight human evaluation
and annotation quality workflow.

The workflow evaluates three output categories:

1. LLM responses;
2. instruction-following responses;
3. structured JSON outputs.

---

## Evaluation Process

### Step 1: Create evaluation cases

Each case contains:

- case ID;
- task type;
- category;
- prompt;
- candidate response;
- reference context;
- expected primary error.

---

### Step 2: Human evaluation

Evaluators score:

- accuracy;
- relevance;
- completeness;
- instruction following.

They also provide:

- primary error label;
- severity;
- confidence;
- written rationale.

---

### Step 3: Validate annotation quality

Pydantic validation checks:

- required fields;
- valid score ranges;
- allowed task types;
- allowed severity values;
- minimum rationale length.

---

### Step 4: Calculate quality scores

The default weighted score is:

- Accuracy: 35%
- Relevance: 25%
- Completeness: 20%
- Instruction Following: 20%

The weights are stored in an external rubric JSON file.

---

### Step 5: Compare evaluators

The agreement module calculates:

- exact error-label agreement;
- exact severity agreement;
- disagreement count;
- disagreement rate;
- average score differences.

The project intentionally avoids unnecessary machine
learning dependencies.

---

### Step 6: Create adjudication queue

Cases are routed for review when:

- primary error labels differ;
- severity labels differ;
- dimension scores differ by two or more points.

The queue includes both evaluator rationales to support
final review.

---

### Step 7: Generate reports

The pipeline produces:

- scored evaluation data;
- quality summary CSV;
- evaluator agreement JSON;
- disagreement/adjudication CSV;
- Markdown evaluation report.

---

## Project Scope

This repository is intentionally small and focused.

It demonstrates practical AI evaluation and annotation QA
skills without attempting to become:

- a model leaderboard;
- a machine learning training pipeline;
- a comprehensive safety benchmark;
- a multimodal computer vision benchmark.

Those areas are better demonstrated through separate,
focused portfolio projects.
