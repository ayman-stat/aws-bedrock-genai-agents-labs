"""Invoke an Amazon Bedrock foundation model with the Converse API."""

from __future__ import annotations

import argparse

from botocore.exceptions import ClientError

from bedrock_labs.config import bedrock_runtime_client, load_config


DEFAULT_PROMPT = "Explain generative AI for a business stakeholder in three concise bullets."


def invoke_converse(prompt: str, system_prompt: str | None = None) -> str:
    """Send a prompt through Bedrock Converse and return generated text."""

    config = load_config()
    client = bedrock_runtime_client()

    request = {
        "modelId": config.model_id,
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

    if system_prompt:
        request["system"] = [{"text": system_prompt}]

    response = client.converse(**request)
    return response["output"]["message"]["content"][0]["text"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Invoke a Bedrock model through Converse.")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="Prompt to send to the model.")
    parser.add_argument("--system", default=None, help="Optional system prompt.")
    args = parser.parse_args()

    config = load_config()
    print(f"Region: {config.region}")
    print(f"Model: {config.model_id}")

    try:
        print(invoke_converse(args.prompt, args.system))
    except ClientError as exc:
        print("Bedrock Converse request failed.")
        print("Check AWS credentials, Region, IAM permissions, and model access.")
        print(f"Reason: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
