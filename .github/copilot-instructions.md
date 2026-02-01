# Copilot instructions for pythonagent

## Project snapshot
- This is a minimal sandbox with a single interactive agent in [agents/jenny.py](agents/jenny.py).
- The agent uses the OpenAI Python SDK and `python-dotenv` (see [requirements.txt](requirements.txt)).

## Architecture and data flow
- Single class `JennyAgent` wraps an `OpenAI` client and a fixed `system_prompt`.
- `JennyAgent.run()` sends a single chat completion request and returns the model output.
- The CLI loop is at the bottom of [agents/jenny.py](agents/jenny.py): read user input → call `run()` → print response.

## Configuration and dependencies
- Required env var: `OPENAI_API_KEY` (loaded via `dotenv.load_dotenv()`).
- Model is hard-coded to `gpt-4o-mini` in `chat.completions.create()`; keep this consistent unless changing behavior explicitly.
- Temperature is set to `0.3` for concise replies.

## Developer workflow
- Run the agent locally with: `python agents/jenny.py` (documented in [README.md](README.md)).
- There are no tests or build steps in this repo.

## Codebase conventions (from actual code)
- Keep the agent logic in the single file [agents/jenny.py](agents/jenny.py) unless expanding the project.
- The prompt style is short and pragmatic; maintain that when editing `system_prompt`.
- The CLI exits on user input `exit` or `quit`.

## When modifying
- If you add new dependencies, update [requirements.txt](requirements.txt).
- If you add new agents or structure, mirror the simple, flat layout used today.