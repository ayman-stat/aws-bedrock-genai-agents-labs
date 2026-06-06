"""Shared configuration helpers for Bedrock labs."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import boto3
from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class BedrockConfig:
    region: str
    model_id: str
    max_tokens: int
    temperature: float
    top_p: float


def load_config() -> BedrockConfig:
    """Load local lab settings from environment variables."""

    return BedrockConfig(
        region=os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION") or "us-east-1",
        model_id=os.getenv("BEDROCK_MODEL_ID", "amazon.nova-micro-v1:0"),
        max_tokens=int(os.getenv("BEDROCK_MAX_TOKENS", "512")),
        temperature=float(os.getenv("BEDROCK_TEMPERATURE", "0.4")),
        top_p=float(os.getenv("BEDROCK_TOP_P", "0.9")),
    )


def bedrock_client(region_name: str | None = None) -> Any:
    """Create a Bedrock control-plane client.

    Returns a boto3 Bedrock client. The return type is platform-specific so it
    is annotated as `Any`.
    """

    config = load_config()
    return boto3.client("bedrock", region_name=region_name or config.region)


def bedrock_runtime_client(region_name: str | None = None) -> Any:
    """Create a Bedrock Runtime client used for model inference.

    Returns a boto3 Bedrock Runtime client (typed as `Any`).
    """

    config = load_config()
    return boto3.client("bedrock-runtime", region_name=region_name or config.region)
