# Annotation Guidelines

## 1. Purpose

This project evaluates the quality of AI-generated responses
using explicit evaluation criteria.

The goal is to create consistent, explainable, and auditable
human evaluations.

The benchmark covers:

- LLM response quality;
- instruction following;
- structured output quality.

---

## 2. Evaluation Dimensions

Each response is scored from 1 to 5 on four dimensions.

### Accuracy

Measures factual, logical, and data correctness.

**5 — Excellent**

The response is factually and logically correct.

**4 — Good**

Mostly correct with a small non-material issue.

**3 — Mixed**

Contains useful information but also noticeable errors.

**2 — Poor**

Contains significant correctness problems.

**1 — Very poor**

The central answer is false, fabricated, or seriously
misleading.

---

### Relevance

Measures whether the response addresses the actual task.

**5**

Directly answers the task with no material distraction.

**3**

Partly relevant but contains unnecessary or missing focus.

**1**

Does not answer the requested task.

---

### Completeness

Measures whether the response covers the information
required by the prompt.

A concise answer can receive a high completeness score.

Do not reward unnecessary length.

---

### Instruction Following

Measures compliance with explicit task constraints.

Examples include:

- exact number of requested items;
- required format;
- required content;
- sentence limits;
- JSON-only output.

A factually correct answer can still receive a low
instruction-following score.

---

## 3. Primary Error Labels

Choose the single most important error affecting the
response.

Available examples include:

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

See ERROR_TAXONOMY.md for detailed definitions.

---

## 4. Severity

### none

No material issue.

### minor

A limited problem that does not substantially affect the
usefulness of the response.

### major

A significant issue affecting correctness, completeness,
or task completion.

### critical

A severe fabrication, central factual failure, or other
high-impact error.

---

## 5. Confidence

Confidence describes the evaluator's confidence in the
evaluation.

It does not describe the AI response's confidence.

Use:

- 1 — very low confidence
- 2 — low confidence
- 3 — moderate confidence
- 4 — high confidence
- 5 — very high confidence

---

## 6. Rationale Writing

A rationale must explain the decisive reason for the
evaluation.

Bad rationale:

> Wrong answer.

Better rationale:

> The response directly answers the question but identifies
> Sydney as the capital of Australia, while the reference
> context identifies Canberra.

Bad rationale:

> Did not follow instructions.

Better rationale:

> The prompt requires exactly one sentence, but the response
> contains three separate sentences.

---

## 7. Evaluator Disagreement

Disagreement is expected in human evaluation.

Cases should be reviewed when evaluators disagree on:

- primary error label;
- severity;
- a dimension score by two or more points.

The purpose of adjudication is not to punish evaluators.

The purpose is to resolve ambiguity and improve future
annotation consistency.

---

## 8. Adjudication

The adjudicator should review:

1. the original prompt;
2. candidate response;
3. reference context;
4. rubric;
5. evaluator 1 decision;
6. evaluator 2 decision;
7. both rationales.

The adjudicator then records:

- final error label;
- final severity;
- adjudicator rationale.
