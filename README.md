# pythonagent

> **👉 New here? Start with [START_HERE.md](START_HERE.md) for a guided introduction to this learning course.**

# Jenny Agent Sandbox

This repo is a lightweight sandbox for building and experimenting with
Python-based AI agents using GitHub Codespaces.

## What this is
- A starter agent ("Jenny")
- A sandbox for prototyping
- A teaching tool for new engineers

## Getting Started

1. Open this repo in GitHub
2. Click Code → Codespaces → Create new Codespace
3. Add OPENAI_API_KEY as a Codespaces Secret
4. Run:

```bash
python agents/jenny.py
```

Talk to Jenny.

Training Center for Python Agents

Alright, this is a great moment to set the tone for your Python Agent Training Center. You’re right: agents are simpler than most enterprise systems you’ve built — the trick is knowing what to ignore.

Below is a practical, opinionated agent cheat sheet you can literally drop into a GitHub repo as a README.md or hand to devs on day one.

⸻

🧠 Python Agent Essentials

A practical cheat sheet for building real agents (not science projects)

⸻

1️⃣ What an Agent Actually Is (no hype)

An agent is just:

A loop that observes → thinks → acts → remembers

That’s it.
No magic. No control plane required.

INPUT → DECISION → ACTION → OUTPUT
              ↘ MEMORY ↗

If someone adds more than this on day one — they’re overengineering.

⸻

2️⃣ The Only Python You Really Need

✅ Must-know Python

These are non-negotiable:
	•	async / await
	•	requests or httpx
	•	dataclasses
	•	typing
	•	json
	•	logging
	•	os / env vars
	•	basic exception handling

🚫 Nice-to-ignore (early on)

You do NOT need:
	•	Metaclasses
	•	Advanced decorators
	•	Async frameworks (FastAPI comes later)
	•	Pandas / NumPy
	•	Complex inheritance trees

Agents love flat code.

⸻

3️⃣ Canonical Agent Folder Structure

This structure scales from hello-world → production:

agent/
├── main.py            # Entry point (the loop)
├── agent.py           # Agent brain
├── llm.py             # LLM calls
├── tools.py           # External actions
├── memory.py          # State handling
├── config.py          # Settings
├── models.py          # Data contracts
└── logging_conf.py    # Logging setup

If it doesn’t fit here, it probably doesn’t belong.

⸻

4️⃣ The Smallest Useful Agent (Baseline)

main.py

import asyncio
from agent import Agent

async def main():
    agent = Agent()
    await agent.run("Summarize this Jira ticket")

if __name__ == "__main__":
    asyncio.run(main())


⸻

agent.py

from llm import ask_llm
from tools import execute_tool
from memory import Memory

class Agent:
    def __init__(self):
        self.memory = Memory()

    async def run(self, input_text: str):
        self.memory.add("user", input_text)

        decision = await ask_llm(self.memory.context())

        result = await execute_tool(decision)

        self.memory.add("agent", result)
        return result

That’s an agent.
Everything else is refinement.

⸻

5️⃣ LLM Layer (Keep It Dumb)

llm.py

import os
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_llm(context: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful agent."},
            {"role": "user", "content": context}
        ]
    )
    return response.choices[0].message.content

Rules
	•	One responsibility
	•	No business logic
	•	No retries here

⸻

6️⃣ Tools = The Agent’s Hands

tools.py

async def execute_tool(decision: str) -> str:
    if "jira" in decision.lower():
        return "Fetched Jira data"
    elif "email" in decision.lower():
        return "Email sent"
    else:
        return "No action taken"

🔑 Rule of thumb

Tools should never think
Agents think, tools execute

⸻

7️⃣ Memory: Keep It Boring

memory.py

class Memory:
    def __init__(self):
        self.messages = []

    def add(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def context(self) -> list:
        return self.messages[-10:]  # sliding window

Don’t overbuild vector DBs until you feel pain.

⸻

8️⃣ Agent Design Patterns (The Only Ones That Matter)

🧹 Janitor Agent
	•	Cleans data
	•	Enforces rules
	•	Never chats
	•	Runs on schedules

📨 Dispatcher Agent
	•	Classifies input
	•	Routes to tools
	•	No memory beyond the task

🧠 Thinker Agent
	•	Multi-step reasoning
	•	Uses memory
	•	Slower, more expensive

🧰 Tool-First Agent
	•	LLM decides which tool
	•	Tools do all real work

⸻

9️⃣ What NOT to Do (Seriously)

❌ Don’t build a framework first
❌ Don’t abstract the LLM too early
❌ Don’t invent a DSL
❌ Don’t let agents talk to agents on day one
❌ Don’t mix business logic into prompts

Agents rot when they get clever too early.

⸻

🔟 Observability (Minimum Viable)

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

Log:
	•	input
	•	decision
	•	tool used
	•	outcome

That’s enough to debug 90%.

⸻

1️⃣1️⃣ Environment Setup (Developer Friendly)

python -m venv .venv
source .venv/bin/activate
pip install openai httpx
export OPENAI_API_KEY=sk-...

No Docker required at first.
Don’t scare people away.

⸻

1️⃣2️⃣ Mental Model to Teach Devs

Agents are microservices with judgment

Same rules:
	•	Stateless when possible
	•	Idempotent tools
	•	Observable behavior
	•	Killable at any time

⸻

1️⃣3️⃣ When You’re Ready to Level Up

Only add these after real usage:
	•	FastAPI wrapper
	•	Redis memory
	•	Kafka triggers
	•	Scheduled runners
	•	Guardrails & validation
	•	Tool schemas

⸻

Final Take (This Is the Line You Put in the Repo)

“If you understand Python async, JSON, and clean functions, you can build agents.
If you don’t — no framework will save you.”

⸻

