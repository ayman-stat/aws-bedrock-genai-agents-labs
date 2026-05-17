# Lab 01: Invoking an Amazon Bedrock Foundation Model

This lab is inspired by Course 1 of the AWS Generative AI and AI Agents with Amazon Bedrock Professional Certificate:

[Getting Started with AWS Generative AI for Developers](https://www.coursera.org/learn/getting-started-aws-generative-ai-developers)

It implements the same learning objective in my own code: invoke an Amazon Bedrock foundation model from Python, inspect the response, and understand the difference between `Converse` and `InvokeModel`.

## What This Lab Demonstrates

- Creating Bedrock and Bedrock Runtime clients with Boto3.
- Listing available foundation models.
- Calling a text model through `Converse`.
- Calling Amazon Nova through `InvokeModel`.
- Reading model output text from the response.
- Avoiding hardcoded credentials and secrets.

## Files

```text
src/bedrock_labs/list_foundation_models.py
src/bedrock_labs/invoke_converse.py
src/bedrock_labs/invoke_model_nova.py
labs/01-invoke-foundation-model/prompts/business_summary_prompt.md
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials using one of the standard AWS SDK methods:

- AWS CLI profile.
- IAM role.
- Environment variables.
- AWS SSO profile.

Do not commit credentials to this repository.

Set environment variables:

```bash
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=amazon.nova-micro-v1:0
```

## Run

List available models:

```bash
python -m bedrock_labs.list_foundation_models
```

Invoke using `Converse`:

```bash
python -m bedrock_labs.invoke_converse --prompt "Explain foundation models to a BI manager."
```

Invoke using `InvokeModel`:

```bash
python -m bedrock_labs.invoke_model_nova --prompt "Summarize Amazon Bedrock for an ML engineer."
```

## Notes

AWS documentation recommends `Converse` when supported because it provides a unified message interface across compatible models. `InvokeModel` remains useful when you need model-native request structures or provider-specific behavior.

## Troubleshooting

Common issues:

- `AccessDeniedException`: IAM policy or model access is missing.
- `ValidationException`: model ID is not available in the selected Region or the payload shape does not match the selected model.
- `UnrecognizedClientException`: AWS credentials are missing or invalid.
- Throttling or quota errors: check Bedrock service quotas and model access.

## Cost Control

- Use short prompts while testing.
- Set low `maxTokens`.
- Stop after validating the request works.
- Review AWS billing and Bedrock usage regularly.
