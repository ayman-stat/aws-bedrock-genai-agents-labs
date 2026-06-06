# Course 1 Notes: Getting Started with AWS Generative AI for Developers

Official course page: [Getting Started with AWS Generative AI for Developers](https://www.coursera.org/learn/getting-started-aws-generative-ai-developers)

Status: **Active / In Progress**

This file summarizes my own study plan and implementation work for Course 1. It does not reproduce Coursera's proprietary exercise text or quizzes.

## Public Course Outline

### Module 1: What is Generative AI?

Main themes:

- Generative AI fundamentals.
- Difference between AI, ML, deep learning, large language models, and foundation models.
- Prompts, inference, and model responses.
- Amazon Bedrock as a managed foundation model service.
- Amazon Q Developer introduction.

My practical goals:

- Understand where Amazon Bedrock fits in the GenAI stack.
- Invoke a foundation model safely from Python.
- Capture what input, output, model ID, and inference configuration mean.
- Keep credentials and cloud costs controlled.

### Module 2: Accessing Amazon Bedrock Foundation Models

Main themes:

- Amazon Bedrock Runtime APIs.
- `InvokeModel`, asynchronous invocation, batch concepts, and `Converse`.
- Foundation model selection.
- Prompt engineering.
- Responsible AI and guardrails.

My practical goals:

- Compare `InvokeModel` and `Converse`.
- Use configurable model IDs and Regions.
- Add basic error handling for AWS permission or model-access issues.
- Document model selection criteria.
- Prepare for guardrails and agent-oriented labs.

## Implemented Lab: Invoking a Foundation Model

Lab folder: [labs/01-invoke-foundation-model](labs/01-invoke-foundation-model/)

Implemented scripts:

- `list_foundation_models.py`: lists available Bedrock foundation models in the configured Region.
- `invoke_converse.py`: invokes a model through the Bedrock `Converse` API.
- `invoke_model_nova.py`: invokes Amazon Nova through the model-native `InvokeModel` payload.

## My Learning Notes

### Bedrock Runtime

Amazon Bedrock Runtime is the API surface used to send prompts to foundation models and receive generated outputs. For text generation, the two core patterns are:

- `Converse`: a unified message-oriented interface for supported models.
- `InvokeModel`: a model-native interface where the request/response shape depends on the model provider.

## Amazon Bedrock Endpoints and API Reference

This repo now includes a dedicated Bedrock API reference document that explains the control-plane and data-plane endpoints used in the course.

- `bedrock`: control-plane endpoint for model and resource management.
- `bedrock-runtime`: data-plane endpoint for real-time inference.
- `bedrock-agent`: control-plane endpoint for agent, prompt template, knowledge base, and flow configuration.
- `bedrock-agent-runtime`: data-plane endpoint for real-time agent execution.

See `docs/amazon_bedrock_endpoints_and_apis.md` for examples of `InvokeModel`, `InvokeModelWithResponseStream`, `StartAsyncInvoke`, `CreateModelInvocationJob`, and recommended handling patterns.

### Model ID

The model ID identifies the foundation model, inference profile, prompt, provisioned throughput, or custom model target. This repo defaults to:

```text
amazon.nova-micro-v1:0
```

That model may not be available in every account or Region, so the scripts allow overriding it with:

```text
BEDROCK_MODEL_ID
```

### Responsible Use

For a professional portfolio repo, the important points are:

- Do not commit AWS credentials.
- Keep generated outputs sanitized.
- Avoid sending private or client data to a model.
- Track cost and Region before running labs.
- Use guardrails when moving beyond simple tests.

## Next Improvements

- Add sanitized sample output after running the lab in AWS.
- Add a guardrails experiment.
- Add a prompt experiment table.
- Add architecture diagram for a simple Bedrock application.
- Add a small business use case connected to analytics or customer retention.
