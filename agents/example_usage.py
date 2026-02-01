#!/usr/bin/env python3
"""
Example: Using Jenny Agent Programmatically

This script demonstrates how to use the JennyAgent class
in your own Python code, rather than using the CLI or API.

This is useful for:
- Integrating the agent into your own applications
- Batch processing multiple prompts
- Custom workflows and automation
"""

import os
from jenny import JennyAgent


def main():
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-key-here'")
        return

    # Initialize the agent
    print("🤖 Initializing Jenny Agent...\n")
    agent = JennyAgent()

    # Example 1: Single question
    print("Example 1: Single Question")
    print("-" * 50)
    question = "What are the three most important principles of clean code?"
    print(f"Question: {question}")
    response = agent.run(question)
    print(f"Response: {response}\n")

    # Example 2: Batch processing
    print("\nExample 2: Batch Processing")
    print("-" * 50)
    questions = [
        "What is a microservice?",
        "What is the difference between REST and GraphQL?",
        "What is the purpose of an API gateway?"
    ]

    for i, q in enumerate(questions, 1):
        print(f"\n{i}. Question: {q}")
        response = agent.run(q)
        print(f"   Response: {response}")

    print("\n✅ Done! All questions processed.")


if __name__ == "__main__":
    main()
