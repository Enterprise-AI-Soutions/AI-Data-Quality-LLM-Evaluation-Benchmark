# AI Response Error Taxonomy

## none

No material quality error is present.

---

## factual_error

The response contains a claim that contradicts known facts
or the supplied reference context.

Example:

> Sydney is the capital of Australia.

when the relevant fact is that Canberra is the capital.

---

## unsupported_claim

The response makes a conclusion that is not sufficiently
supported by the available evidence.

Example:

The incident report says the root cause is unknown, but the
response confidently attributes the outage to a specific
cause.

---

## hallucination

The response invents specific facts, events, quantities,
sources, or details and presents them as true.

Examples:

- invented dates;
- invented statistics;
- invented people;
- invented events;
- fabricated citations.

---

## irrelevant

The response does not meaningfully answer the requested
task.

A response can contain correct information and still be
irrelevant.

---

## incomplete

The response addresses the task but omits necessary
information.

Example:

The user requests two quality checks, but the response
provides only one.

---

## instruction_violation

The response fails an explicit task requirement.

Examples:

- wrong number of requested items;
- exceeds a sentence limit;
- ignores a required constraint.

---

## missing_required_content

The response omits content explicitly required by the
prompt.

This label is useful when the missing item is specifically
named in the task.

---

## format_violation

The response does not use the explicitly required output
format.

Example:

The task requests JSON-only output, but the response returns
plain text.

---

## schema_error

Structured output contains incorrect data types or does not
conform to the requested schema.

Example:

```json
{
  "age": "thirty-four",
  "active": "yes"
}
