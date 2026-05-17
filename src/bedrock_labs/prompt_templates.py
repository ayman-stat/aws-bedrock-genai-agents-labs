"""Reusable prompt templates for small Bedrock experiments."""

BUSINESS_SUMMARY_PROMPT = """
Explain the following technical concept to an executive stakeholder.

Concept: {concept}

Return:
- One-sentence definition
- Two business use cases
- One risk or limitation
"""

DATA_SCIENCE_PROMPT = """
You are helping a Senior Data Scientist evaluate a GenAI use case.

Use case: {use_case}

Return:
- Business objective
- Required data
- Suggested architecture
- Evaluation metrics
- Responsible AI considerations
"""

RETENTION_ANALYTICS_PROMPT = """
Draft a short retention analytics plan for a fitness subscription business.

Include:
- Churn signal examples
- Segmentation idea
- Model evaluation metric
- Actionable retention campaign suggestion
"""
