# Step 2: Turning the Jenny Python Agent into a REST API



## Purpose



This document explains how to take an existing **Python-based CLI AI agent** (Jenny)

and expose it as a **REST API** using FastAPI, without rewriting the agent logic.



This pattern allows:

- CLI execution (local development, debugging)

- HTTP-based execution (microservice, Jenkins, other systems)

- Clean separation between **agent logic** and **transport layer**



---



## Architecture Overview



The design follows a simple and intentional separation of concerns:

┌───────────────────────┐

│   Transport Layer     │

│  (CLI / REST / etc.)  │

└──────────┬────────────┘

│

▼

┌───────────────────────┐

│     Agent Core        │

│  (Prompt + OpenAI)    │

└───────────────────────┘

- The **agent core** knows nothing about HTTP

- The **API layer** knows nothing about OpenAI internals

- Both reuse the same agent function



---



## Recommended File Structure



```text

jenny-agent-sandbox/

├── jenny_agent.py        # Agent core logic (CLI + reusable function)

├── jenny_api.py          # FastAPI REST wrapper

├── requirements.txt

├── README.md

└── .env









Step 1: Refactor the Agent for Reuse







jenny_agent.py





The agent must expose a callable function (e.g. run_jenny)

and optionally still support CLI execution.

def run_jenny(prompt: str) -> str:

    """

    Core agent logic.

    Calls OpenAI and returns a response.

    """

    # OpenAI call logic here

    return response





if __name__ == "__main__":

    user_prompt = input("Ask Jenny: ")

    print(run_jenny(user_prompt))



Key Points





run_jenny() is reusable by any transport
CLI mode still works via python jenny_agent.py
No HTTP logic lives here










Step 2: Create the REST API Wrapper







New File: 

jenny_api.py





This file exposes the agent as an HTTP service using FastAPI.

from fastapi import FastAPI

from pydantic import BaseModel

from jenny_agent import run_jenny



app = FastAPI(title="Jenny Agent API")



class JennyRequest(BaseModel):

    prompt: str



class JennyResponse(BaseModel):

    response: str



@app.post("/jenny", response_model=JennyResponse)

def call_jenny(req: JennyRequest):

    result = run_jenny(req.prompt)

    return JennyResponse(response=result)



Design Notes





No OpenAI logic here
No prompt construction here
This file only:
Accepts input
Calls the agent
Returns output











Step 3: Install Dependencies





Add to requirements.txt:

fastapi

uvicorn

pydantic

Install dependencies:

pip install -r requirements.txt









Step 4: Run the API Server





Start the FastAPI server:

uvicorn jenny_api:app --host 0.0.0.0 --port 880



What This Does





Starts a long-running HTTP server
Keeps the agent alive
Listens for incoming requests
Does NOT run the agent until called










Step 5: Call the Agent via REST







Using curl (Command Line)



curl -X POST http://localhost:880/jenny \

  -H "Content-Type: application/json" \

  -d '{

    "prompt": "Explain what Jenny does in one sentence."

  }'

Example response:

{

  "response": "Jenny is a lightweight Python-based AI agent designed to process prompts and return intelligent responses."

}









Step 6: Use FastAPI Swagger UI (Recommended)





FastAPI automatically provides API documentation.



Open in a browser:

http://localhost:880/docs

From here you can:



Test requests
View schemas
Demo the service
Validate inputs










CLI vs REST: Execution Model Comparison



Mode

Command

Behavior

CLI

python jenny_agent.py

Runs once, exits

REST

uvicorn jenny_api:app

Long-running service

REST Call

POST /jenny

Runs agent per request

Both modes call the same agent function.









Common Mistakes to Avoid





❌ Putting OpenAI logic in jenny_api.py
❌ Hardcoding prompts in the API layer
❌ Using GET with query parameters for agent input
❌ Coupling HTTP logic to agent logic










Why This Pattern Matters





This approach:



Scales from local dev → microservice
Works with Jenkins, GitHub Actions, and other systems
Keeps costs predictable
Enables future transports (Kafka, cron, batch jobs)
Matches enterprise microservice design principles










Next Logical Enhancements (Optional)





/health endpoint
Request IDs and logging
Cost-per-request tracking
Rate limiting
Authentication headers
Jenkins pipeline integration










Summary





The agent remains a pure Python component
FastAPI acts as a thin transport layer
CLI and REST coexist cleanly
No rework required as the system grows




This is the canonical foundation for an agent-as-a-service architecture.

