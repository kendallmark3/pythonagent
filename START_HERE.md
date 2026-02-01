# START HERE — Jenny Agent Learning Course  
### Learn → Teach → Master → Scale

Welcome. This repository is both a **hands-on learning course** and a **real foundation** for building AI-powered agents that run safely in modern software platforms.

This is not a toy demo.  
This is not a framework tutorial.  
This is how *real* agent systems are built — step by step.

---

## What This Repository Is

This repo is a **learning center** for:

- Building Python-based AI agents
- Understanding what makes an agent *real*
- Exposing agents as services
- Running agents safely in modern environments
- Progressing from simple reasoning → true agent behavior

The course follows a deliberate progression:

1. **Learn** — Understand the fundamentals
2. **Teach** — Share patterns and reinforce clarity
3. **Master** — Add complexity intentionally
4. **Scale** — Prepare for real platforms and orchestration

---

## What This Repository Is NOT

- Not a magic "autonomous agent" demo
- Not a no-code AI product
- Not a framework-first experiment
- Not production automation out of the box

We value:
- Clarity over cleverness
- Control over chaos
- Architecture over hype

---

## Prerequisites

You do **not** need:
- Kubernetes knowledge
- Cloud accounts
- Infrastructure access
- Paid tools beyond minimal AI usage

You **do** need:
- A GitHub account
- Basic Python familiarity
- Curiosity and discipline

---

## Development Environment (Recommended)

This course is designed to run in **GitHub Codespaces**.

Why Codespaces:
- One-click setup
- Identical environment for everyone
- No "works on my machine" issues
- Safe sandbox for experimentation

### Getting Started with Codespaces

1. Open this repository in GitHub
2. Click **Code**
3. Select **Open with Codespaces**
4. Create a new Codespace

You are now ready to begin.

---

## OpenAI API Access (Required)

This course uses OpenAI APIs for agent reasoning.

### Step 1: Create an OpenAI Account

Go to:  
👉 https://platform.openai.com/

Sign up or log in.

---

### Step 2: Add a Small Credit Balance

For this course:
- **$5 is more than enough**
- Simple prompts are very cheap
- You will not burn through credits quickly

This is intentional — cost awareness is part of the learning.

---

### Step 3: Create an API Key

1. Go to the OpenAI dashboard
2. Create a new API key
3. Copy the key somewhere safe (you will not see it again)

---

## Setting Your API Key (Important)

We intentionally **do not** use `.env` files in this course.

This is a teaching choice.

### Set the API Key in Your Shell

In your Codespaces terminal:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

That's it.

### Why This Is Safe

- The key lives only in your shell
- It is not written to disk
- It is not committed to Git
- It disappears when the Codespace stops
- Other developers cannot see it

This mirrors how real platforms inject secrets at runtime.

---

## First Run (Smoke Test)

Once your API key is set:

```bash
cd agents
python jenny.py
```

You should:
- Be prompted for input
- See an AI-generated response
- Confirm everything works end-to-end

If this works, you are officially ready to start.

---

## Course Structure (High-Level)

This repository is organized around progressive steps:

### Step 1 — Local Agent (CLI)
- Single-shot reasoning
- Prompt discipline
- Cost awareness
- Clean agent core

### Step 2 — Agent as a REST API
- FastAPI wrapper
- Service boundaries
- Contracts and schemas
- Machine-to-machine invocation

### Step 3 — Agent as an Internal Microservice
- Ingress concepts
- Webhooks
- Event-driven invocation
- Enterprise-safe deployment model

### Step 4 — Becoming a True Agent
- Memory (introduced intentionally)
- Tools and actions
- Bounded loops
- Optional frameworks (e.g., LangChain)

Each step builds on the previous one.  
Nothing is thrown away.

---

## How to Use This Repository as a Course

### For Individual Learners
- Follow the steps in order
- Read the markdown files
- Run the code
- Experiment freely
- Break things safely

### For Teams
- Fork the repo
- Use Codespaces per developer
- Discuss architectural choices
- Compare implementations
- Teach each other

### For AI-Assisted Learning

This repo is intentionally structured so that:
- An AI can read it
- Understand the progression
- Assist with extensions
- Help generate variations

---

## Rules of the Road (Important)

- Never commit API keys
- Never log secrets
- Never add autonomy without guardrails
- Always prefer clarity over cleverness
- If it doesn't work cleanly in Codespaces, it's not ready

---

## Why This Course Exists

Most "agent tutorials" skip the hard parts:
- Boundaries
- Safety
- Cost
- Architecture
- Enterprise reality

This course exists to fix that.

By the end, you won't just know how to build an agent —  
you'll know why it works, when it's safe, and how it scales.

---

## Where to Go Next

Once this file makes sense:
- Read the [agents/README.md](agents/README.md) for hands-on instructions
- Read [docs/Learn.md](docs/Learn.md) for the full architecture
- Move forward deliberately

You're not learning a tool.

You're learning a way of thinking.

**Welcome to the course.**
