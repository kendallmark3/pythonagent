# Jenny Agent - Getting Started

This directory contains the Jenny Agent implementation, a Python-based AI agent that can be run as a CLI tool or as a REST API service.

## Prerequisites

1. Python 3.12+ installed
2. OpenAI API key (get one at https://platform.openai.com/api-keys)
3. Dependencies installed (see Installation below)

## Installation

Install the required dependencies:

```bash
cd /home/runner/work/pythonagent/pythonagent
pip install -r requirements.txt
```

## Configuration

Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Note**: This is intentionally NOT using a `.env` file to mirror how real platforms inject secrets at runtime. The key is never written to disk and is not committed to Git.

## Usage

### Option 1: CLI Mode (Step 1)

Run Jenny as an interactive command-line agent:

```bash
cd agents
python jenny.py
```

You'll see a prompt where you can type questions. Type `exit` or `quit` to stop.

**Example session:**
```
🤖 Jenny Agent started. Type 'exit' to quit.

You: What is the purpose of this agent?
Jenny: I'm a helpful engineering assistant designed to reason step-by-step and provide concise, practical answers to your questions.

You: exit
👋 Jenny signing off.
```

### Option 2: REST API Mode (Step 2)

Run Jenny as an HTTP API service:

```bash
cd agents
uvicorn jenny_api:app --host 0.0.0.0 --port 8800
```

The API will be available at `http://localhost:8800`

**Interactive API Documentation:**
- Swagger UI: http://localhost:8800/docs
- ReDoc: http://localhost:8800/redoc

**Example API call with curl:**

```bash
curl -X POST http://localhost:8800/jenny \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain what this agent does in one sentence."
  }'
```

**Example response:**
```json
{
  "response": "I am Jenny, a helpful engineering assistant that provides concise, practical answers through step-by-step reasoning."
}
```

**Health check:**
```bash
curl http://localhost:8800/health
```

## Architecture

### CLI Mode (Step 1)
- **File**: `jenny.py`
- **Execution**: One-shot, exits after each run
- **Use Case**: Local development, debugging, experimentation

### API Mode (Step 2)
- **File**: `jenny_api.py`
- **Execution**: Long-running service
- **Use Case**: Microservice integration, CI/CD pipelines, machine-to-machine invocation

Both modes use the same core `JennyAgent` class, demonstrating clean separation between agent logic and transport layer.

## Cost Awareness

- Each API call costs a small amount based on your OpenAI pricing
- The model used is `gpt-4o-mini` which is cost-effective
- Temperature is set to 0.3 for concise responses
- Monitor your usage in the OpenAI dashboard

## Troubleshooting

**Error: "The api_key client option must be set"**
- Make sure you've set the `OPENAI_API_KEY` environment variable
- Verify the key is correct (no extra spaces or quotes)

**Error: "Module not found"**
- Ensure you've installed dependencies: `pip install -r requirements.txt`
- Make sure you're in the correct directory

**API server not starting**
- Check if port 8800 is already in use
- Try a different port: `uvicorn jenny_api:app --port 8801`

## Next Steps

After mastering the CLI and API modes, proceed to:
- Step 3: Deploy as an internal microservice
- Step 4: Add memory and tool capabilities
- Explore the documentation in `/docs` for advanced patterns

## Learn More

- [Learn.md](../docs/Learn.md) - Full architecture walkthrough
- [Teach.md](../docs/Teach.md) - Step 2 details (REST API)
- [Master.md](../docs/Master.md) - Advanced agent concepts
