# Amazon Bedrock Endpoints and APIs

This document explains the main Amazon Bedrock endpoints and the API patterns used throughout the AWS Bedrock certificate labs.

## Amazon Bedrock Endpoints

Amazon Bedrock separates control-plane and data-plane functionality into specialized endpoints.

- `bedrock`
  - Control plane for core model and resource management.
  - Use it for administrative actions such as listing available models, managing access, or viewing metadata.

- `bedrock-runtime`
  - Data plane for real-time model inference.
  - Use it when calling a model to generate text, audio, image, video, or other inference output.

- `bedrock-agent`
  - Control plane for managing agents, prompt templates, knowledge bases, and prompt flows.
  - Use it when you create or configure an agent, knowledge base, or flow.

- `bedrock-agent-runtime`
  - Data plane for agent execution and runtime queries.
  - Use it when invoking an agent or a prompt flow in real time.

## Amazon Bedrock API Patterns

### InvokeModel API

- Purpose: Synchronous model invocation for immediate responses.
- Key features: single request-response pattern, direct model interaction.
- Best for: chatbots, interactive applications, real-time content generation.

Example:

```python
import json
import boto3

client = boto3.client('bedrock-runtime')
response = client.invoke_model(
    modelId='amazon.titan-text-express-v1',
    body=json.dumps({
        'inputText': 'explain quantum computing',
        'textGenerationConfig': {
            'maxTokenCount': 500,
            'temperature': 0.5,
            'topP': 0.9,
        },
    }),
)

payload = json.loads(response['body'].read())
print(payload)
```

### InvokeModelWithResponseStream API

- Purpose: Streaming responses for better user experience.
- Benefits: real-time text generation, improved interactivity, partial output while the model is still generating.
- Best for: interactive chat applications, live text generation displays.

Example:

```python
import json
import boto3

client = boto3.client('bedrock-runtime')
response = client.invoke_model_with_response_stream(
    modelId='amazon.titan-text-express-v1',
    body=json.dumps({
        'inputText': 'explain quantum computing',
        'textGenerationConfig': {
            'maxTokenCount': 500,
            'temperature': 0.5,
            'topP': 0.9,
        },
    }),
)

for event in response.get('body', []):
    if 'chunk' in event and 'bytes' in event['chunk']:
        chunk = json.loads(event['chunk']['bytes'])
        print(chunk.get('outputText', ''), end='', flush=True)
```

### StartAsyncInvoke API

- Purpose: Asynchronous processing for time-consuming or long-running tasks.
- Key features: returns a job invocation ARN immediately, background processing, progress tracking, no long-lived client connection.
- Best for: video generation, audio generation, complex analysis, heavy compute tasks.

Example:

```python
import boto3
import random

bedrock_runtime = boto3.client('bedrock-runtime')
seed = random.randint(0, 2147483646)

response = bedrock_runtime.start_async_invoke(
    modelId='amazon.nova-reel-v1:0',
    modelInput={
        'taskType': 'TEXT_VIDEO',
        'textToVideoParams': {'text': 'A robot painting a sunset'},
        'videoGenerationConfig': {
            'fps': 24,
            'durationSeconds': 6,
            'dimension': '1280x720',
            'seed': seed,
        },
    },
    outputDataConfig={
        's3OutputDataConfig': {
            's3Uri': 's3://<bucket_name>/<prefix>/',
        },
    },
)

print(response['invocationArn'])
```

### CreateModelInvocationJob API

- Purpose: Batch processing for large-scale operations.
- Key features: S3 integration, parallel processing support, orchestration of large jobs, efficient use of compute.
- Best for: bulk content processing, customer support ticket analysis, large dataset classification, automated content enrichment.

Example:

```python
import boto3

bedrock = boto3.client('bedrock')

response = bedrock.create_model_invocation_job(
    roleArn='arn:aws:iam::<account>:role/<bedrock-invoke-role>',
    modelId='anthropic.claude-3-haiku-20240307-v1:0',
    jobName='support-ticket-analysis',
    inputDataConfig={
        's3InputDataConfig': {
            's3Uri': 's3://<bucket_name>/<input_file>.jsonl',
        },
    },
    outputDataConfig={
        's3OutputDataConfig': {
            's3Uri': 's3://<bucket_name>/<output-prefix>/',
        },
    },
)

print(response['jobArn'])
```

## Best Practices for API Usage

### Error Handling

Use structured error handling for validation issues, timeouts, and unexpected failures.

Example:

```python
import json
import boto3

bedrock_runtime = boto3.client('bedrock-runtime')


def safe_model_invoke(prompt, model_id):
    try:
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=json.dumps({
                'inputText': prompt,
                'textGenerationConfig': {
                    'maxTokenCount': 512,
                    'temperature': 0.7,
                },
            }),
        )
        return json.loads(response['body'].read())
    except bedrock_runtime.exceptions.ValidationException:
        print('Invalid request parameters')
    except bedrock_runtime.exceptions.ModelTimeoutException:
        print('Model inference timed out')
    except Exception as e:
        print(f'Unexpected error: {e}')
```

### Rate Limiting and Retries

- Implement exponential backoff when retrying on throttling.
- Avoid burst traffic by pacing requests.
- Monitor service quotas and adjust request frequency.

### Response Handling

- Different models may return different response shapes.
- Text models return JSON with generated text.
- Image and video models may return S3 references or base64-encoded payloads.
- Streaming responses deliver chunks that should be assembled.

### Model Selection and Versioning

- Use explicit model IDs, such as `anthropic.claude-v2` or `amazon.titan-text-express-v1`.
- Models are versioned; specify the exact version when possible.
- Review model capabilities, pricing, and token limits before choosing.

### API Limits and Quotas

- Know the token limit for your chosen model.
- Track concurrency and request-per-second quotas.
- Use retry logic to handle temporary throttling.
- Keep prompt sizes and output length under control.

## Recommended Project Assets

This repo now provides:

- `docs/amazon_bedrock_endpoints_and_apis.md`
- `genai-exercise1-bedrock-api-overview.ipynb`
- `genai-exercise1-bedrock-batch.ipynb`
