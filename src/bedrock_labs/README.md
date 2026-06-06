Utilities and examples for Amazon Bedrock labs.

Usage examples:

List available models:

```bash
python -m bedrock_labs.list_foundation_models
```

Invoke a model with Converse:

```bash
python -m bedrock_labs.invoke_converse --prompt "Explain foundation models to a BI manager."
```

Invoke a Nova model with InvokeModel:

```bash
python -m bedrock_labs.invoke_model_nova --prompt "Summarize Amazon Bedrock for a data scientist."
```

Configuration is controlled via environment variables or a local `.env` file:

- `AWS_REGION` or `AWS_DEFAULT_REGION`
- `BEDROCK_MODEL_ID`
- `BEDROCK_MAX_TOKENS`, `BEDROCK_TEMPERATURE`, `BEDROCK_TOP_P`
