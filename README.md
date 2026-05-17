# AWS Bedrock Generative AI and AI Agents Labs

Personal learning and portfolio repository for the **AWS Generative AI and AI Agents with Amazon Bedrock Professional Certificate** on Coursera.

This repository is intentionally marked as **in progress**. It contains my own lab code, notes, and implementation templates while linking back to the official Coursera and AWS documentation. It does not copy Coursera exercise text, quizzes, or proprietary course material.

## Certificate Status

**In Progress**

Official certificate page: [AWS Generative AI and AI Agents with Amazon Bedrock Professional Certificate](https://www.coursera.org/professional-certificates/aws-generative-ai-developers)

## Course Roadmap

| Course | Status | Focus |
| --- | --- | --- |
| Getting Started with AWS Generative AI for Developers | Active / In Progress | Amazon Bedrock fundamentals, foundation model invocation, prompt engineering, responsible AI basics |
| Generative AI Applications with Amazon Bedrock | In Progress / Planned | Knowledge bases, RAG, agents, orchestration, enterprise GenAI workflows |
| Amazon Bedrock Customization, Optimization & Automation | In Progress / Planned | Evaluation, optimization, fine-tuning concepts, automation, LangChain, token optimization |

## Current Implemented Lab

### Course 1: Invoke an Amazon Bedrock Foundation Model

This lab implements the core idea behind invoking an Amazon Bedrock foundation model from Python using Boto3.

Implemented examples:

- List available foundation models in the configured AWS Region.
- Invoke a text model using the Amazon Bedrock `Converse` API.
- Invoke a model using the native `InvokeModel` API payload for Amazon Nova.
- Keep credentials out of the repository through local AWS configuration and environment variables.

Start here: [labs/01-invoke-foundation-model](labs/01-invoke-foundation-model/)

## Repository Structure

```text
src/bedrock_labs/                 Reusable Python utilities and runnable examples
labs/01-invoke-foundation-model/  Course 1 lab: invoke a foundation model
labs/02-amazon-q-developer/       Placeholder for Amazon Q Developer practice
labs/03-bedrock-guardrails/       Placeholder for Bedrock Guardrails practice
notes/                            Original study notes and reflections
docs/                             Security, responsible AI, and setup notes
```

## Quick Start

Prerequisites:

- AWS account with Bedrock access.
- IAM user or role with permissions for Amazon Bedrock model invocation.
- Model access enabled in the AWS Region you use.
- Python 3.10+.

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Configure environment:

```bash
cp .env.example .env
```

Set:

```text
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=amazon.nova-micro-v1:0
```

Run examples:

```bash
python -m bedrock_labs.list_foundation_models
python -m bedrock_labs.invoke_converse --prompt "Explain generative AI for a business stakeholder in 3 bullets."
python -m bedrock_labs.invoke_model_nova --prompt "Write a one-paragraph summary of Amazon Bedrock."
```

## Why This Repo Is Professional

It is acceptable to show active study when it is transparent and connected to real implementation. This repo is meant to demonstrate:

- Hands-on AWS Bedrock API practice.
- Responsible handling of credentials and cloud costs.
- Practical GenAI application thinking.
- Progress toward AI agent and enterprise GenAI skills.
- Alignment with Senior Data Scientist, ML Engineer, AI Engineer, and Analytics Lead roles.

## References

- Coursera certificate: [AWS Generative AI and AI Agents with Amazon Bedrock Professional Certificate](https://www.coursera.org/professional-certificates/aws-generative-ai-developers)
- Course 1: [Getting Started with AWS Generative AI for Developers](https://www.coursera.org/learn/getting-started-aws-generative-ai-developers)
- AWS Bedrock Python examples: [Run example Amazon Bedrock API requests through Boto3](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-ex-python.html)
- AWS Bedrock inference APIs: [Submit prompts and generate responses using the API](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-api.html)

## Confidentiality

No employer, client, freelance, Leejam, IDH, Huawei, banking, Upwork, or InteriorAiMVP private data should be committed to this repository.
