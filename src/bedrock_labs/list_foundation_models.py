"""List Amazon Bedrock foundation models available in the configured Region."""

from __future__ import annotations

from botocore.exceptions import ClientError

from bedrock_labs.config import bedrock_client, load_config


def list_foundation_models() -> list[dict]:
    """Return model summaries from the Bedrock control plane."""

    client = bedrock_client()
    response = client.list_foundation_models()
    return response.get("modelSummaries", [])


def main() -> None:
    config = load_config()
    print(f"Region: {config.region}")

    try:
        models = list_foundation_models()
    except ClientError as exc:
        print("Unable to list foundation models.")
        print(f"Reason: {exc}")
        raise SystemExit(1) from exc

    if not models:
        print("No models returned. Check Region and Bedrock account access.")
        return

    for model in models:
        provider = model.get("providerName", "Unknown provider")
        model_name = model.get("modelName", "Unknown model")
        model_id = model.get("modelId", "Unknown model ID")
        modalities = ", ".join(model.get("outputModalities", []))
        print(f"- {provider}: {model_name} | {model_id} | outputs: {modalities}")


if __name__ == "__main__":
    main()
