"""Invoke Amazon Nova through the Bedrock InvokeModel API."""

from __future__ import annotations

import argparse
import json

from botocore.exceptions import ClientError

from bedrock_labs.config import bedrock_runtime_client, load_config


DEFAULT_PROMPT = "Write a one-paragraph summary of Amazon Bedrock for a data scientist."


def invoke_model_nova(prompt: str) -> str:
    """Invoke a Nova text model with its native request payload."""

    config = load_config()
    client = bedrock_runtime_client()

    native_request = {
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ],
        "inferenceConfig": {
            "maxTokens": config.max_tokens,
            "temperature": config.temperature,
            "topP": config.top_p,
        },
    }

    response = client.invoke_model(
        modelId=config.model_id,
        body=json.dumps(native_request),
        accept="application/json",
        contentType="application/json",
    )
    model_response = json.loads(response["body"].read())
    return model_response["output"]["message"]["content"][0]["text"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Invoke a Bedrock model through InvokeModel.")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="Prompt to send to the model.")
    args = parser.parse_args()

    config = load_config()
    print(f"Region: {config.region}")
    print(f"Model: {config.model_id}")

    try:
        print(invoke_model_nova(args.prompt))
    except ClientError as exc:
        print("Bedrock InvokeModel request failed.")
        print("Check AWS credentials, Region, IAM permissions, and model access.")
        print(f"Reason: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
