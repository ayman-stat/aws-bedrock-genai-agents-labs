# Responsible AI Checklist

Use this checklist before publishing or presenting any Bedrock experiment.

## Input Data

- [ ] No personal, employer, client, banking, healthcare, or confidential data is included.
- [ ] Dataset source is public, synthetic, or explicitly allowed.
- [ ] Prompt does not reveal secrets, credentials, internal URLs, or private business logic.

## Model Output

- [ ] Output is reviewed before sharing.
- [ ] Hallucination risk is acknowledged.
- [ ] Any generated recommendation is positioned as decision support, not final authority.
- [ ] Sensitive or harmful output is filtered or excluded.

## Evaluation

- [ ] Prompt objective is clear.
- [ ] Expected output format is defined.
- [ ] Response quality is reviewed against business needs.
- [ ] Failure cases are documented.

## Production Readiness

- [ ] Guardrails are considered.
- [ ] Logging avoids sensitive content.
- [ ] Cost and latency are monitored.
- [ ] Human review is included for high-impact decisions.
