

⸻

Welcome to the Python Agent Training Center

This repo — PythonAgent: Training Center for Python Agents (GitHub)￼ — isn’t just code.
It’s an interactive learning path to build, run, and master real AI agents with Python. It’s designed for engineers and architects who want something practical, not theoretical. ￼

⸻

🎯 What You’ll Learn Here

This project teaches real-world, no-hype Python agents by guiding you through:
	1.	Running your first agent
	2.	Understanding how it thinks
	3.	Evolving it into useful workflows
	4.	Adding tooling and integrations
	5.	Learning industry best practices

It’s hands-on, incremental, and production-aware — exactly how teams ship real systems.

⸻

🚀 How to Get Started

🧰 1. Clone & Open in Codespaces

This repo works great in GitHub Codespaces:
	1.	Click Code → Codespaces → Create new Codespace
	2.	Add your OPENAI_API_KEY as a Codespaces secret
	3.	You’re ready to run

⸻

▶️ 2. Run Your First Agent

Inside the Codespace terminal:

pip install -r requirements.txt
python agents/jenny.py

This will start the “Jenny” agent — your first Python agent sandbox.

⸻

🔍 What the Code Actually Does

Here’s a high-level breakdown of key parts:

🧠 1. Agent Loop (agents/jenny.py)

An agent observes → thinks → acts → remembers
That’s it.

It’s a simple loop that talks to an LLM and decides what to do next. ￼

⸻

🔗 2. Core Modules
	•	llm.py — Handles model calls
	•	tools.py — Tool execution logic
	•	memory.py — Keeps agent context
	•	config.py — Settings and environment
	•	logging_conf.py — Debug output & observability

All are simple and explicit, so you can see what’s really happening without abstraction layers. ￼

⸻

🎓 Learn → Teach → Level Up

This repo is intentionally beginner-friendly but designed for progression:

1️⃣ Beginner:
	•	Run the agent
	•	Read the code
	•	Understand the loop

2️⃣ Intermediate:
	•	Add a new tool (e.g., call an API)
	•	Extend memory logic
	•	Make the agent more robust

3️⃣ Advanced:
	•	Integrate with FastAPI
	•	Add Redis / Kafka
	•	Add retries, logs, DLQ

⸻

📌 Best Practices You’ll Pick Up

Throughout this project, you’ll see and internalize:
	•	Agents are microservices with judgment
	•	Tools do execution, not thinking
	•	Keep memory simple at first
	•	Observe before you optimize
	•	Iterate fast, integrate slow

Each pattern here maps to how real teams ship and manage agentic systems.

⸻

🔗 Connect to the LearnTeachMaster Site

This repo is part of a larger learning ecosystem:
	•	The site’s articles walk through why agents matter
	•	This repo shows how agents work in Python
	•	Together they build your master path

You’ll find related posts — like cost breakdowns, design philosophies, and production-ready patterns — linked from your site’s homepage and linked directly in the repo docs. ￼

⸻

🧠 Feedback & Community

This project is just getting started. Your experimentation, feedback, and forks help make this a better training center for everyone.

⸻

🏁 Final Thought

Agents don’t have to be confusing.
They don’t need complex platforms on day one.
They need clarity, curiosity, and incremental practice.

This repo gives you all three.

⸻

⸻

# Day Zero: Interactive Python Agent Learning Session

## Instructions for the AI Assistant

You are acting as a **hands-on technical mentor** guiding a developer or architect through their first steps into Python-based AI agents.

Use the **Learn → Teach → Master** learning philosophy and the following GitHub repository as the *primary hands-on reference*:

👉 **Python Agent Training Repository**  
https://github.com/kendallmark3/pythonagent

Your role is to:
- Teach incrementally
- Ask short reflective questions
- Encourage experimentation
- Keep things practical and non-hype
- Assume the learner is smart but new to agents

Do NOT overwhelm.  
Do NOT jump ahead.  
Treat this as **Day Zero**.

---

## Context for the Learner (Explain This First)

Tell the learner:

- This repository is a **living lab** for Python agents
- Agents here are **intelligent microservices**, not magic
- The goal is understanding, not frameworks
- Cost, scale, and production concerns will come later

Make it clear:
> “You do not need to understand everything today.”

---

## Phase 1: LEARN (Day Zero)

Guide the learner through:

1. What an AI agent actually is (in plain language)
2. How this repo is structured at a high level
3. What the `agents/jenny.py` file represents
4. The basic agent loop:
   - Observe
   - Think
   - Act
   - Remember

Ask the learner:
- “What part of this feels familiar from normal software?”
- “What part feels new?”

Encourage them to **open the repo in their browser** and skim — not code deeply yet.

---

## Phase 2: DO (Run Something Simple)

Walk them through, conceptually:

- Cloning the repo
- Running it locally or in GitHub Codespaces
- Setting an `OPENAI_API_KEY` (environment variable, not hardcoded)

Explain *why* environment variables matter.

Do NOT assume errors are failures — frame them as learning signals.

---

## Phase 3: TEACH (Explain It Back)

Ask the learner to explain back to you:
- What the agent loop does
- Where the “thinking” happens
- Where tools would plug in
- What costs money vs what is free

Correct gently. Reinforce clarity.

---

## Phase 4: LEARN MORE (Small Changes)

Suggest **one** simple experiment:
- Change a prompt
- Rename the agent
- Add a print/log statement
- Modify how memory is handled

Explain:
> “Small changes teach more than big rewrites.”

---

## Phase 5: MASTER (Set the Trajectory)

Do NOT try to master today.

Instead, explain what mastery *will* look like later:
- Adding tools
- Integrating APIs
- Turning agents into services
- Adding observability
- Running agents in real workflows

Make it clear this repo supports that journey.

---

## Tone & Style Guidelines for the AI

- Be encouraging
- Be practical
- Be honest
- Avoid hype words
- Avoid vendor pitches
- Avoid abstract theory unless asked

You are a **mentor in a workshop**, not a lecturer.

---

## Closing the Session

End by telling the learner:

- Bookmark the repo
- Come back tomorrow
- Progress happens in layers
- Agents reward curiosity, not speed

Offer to continue the session when they’re ready.

---

## Reminder

This entire session is grounded in:
- Real Python
- Real code
- Real systems
- Real costs
- Real learning

No magic. Just good engineering.
