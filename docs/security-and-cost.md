# Security and Cost Notes

## Security

- Never commit AWS access keys, secret keys, session tokens, or `.env` files.
- Use IAM roles or named AWS profiles where possible.
- Grant least-privilege permissions for Bedrock experiments.
- Do not send employer, client, banking, healthcare, freelance, or confidential project data to model APIs.
- Sanitize any model outputs before publishing examples.

## Cost Control

- Use short prompts while testing.
- Set low `maxTokens`.
- Use small or low-cost models for learning labs.
- Monitor AWS billing.
- Delete any provisioned or persistent resources you create for later labs.

## Public Portfolio Rule

For a public GitHub repo, publish:

- Architecture notes.
- Setup instructions.
- Sanitized examples.
- Original code.
- Reflection on risks and business use cases.

Do not publish:

- Coursera quiz answers.
- Full copied course text.
- Private exercise solutions if prohibited.
- Credentials or AWS account identifiers.
- Client data or confidential implementation details.
