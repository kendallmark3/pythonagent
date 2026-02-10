#!/usr/bin/env python3
"""
Example: Calling Jenny Agent via REST API

This script demonstrates how to call the Jenny Agent
when it's running as a REST API service.

Prerequisites:
1. Start the API server in another terminal:
   cd agents
   uvicorn jenny_api:app --host 0.0.0.0 --port 8800

2. Run this script:
   python example_api_client.py
"""

import requests
import json


def call_jenny_api(prompt: str, base_url: str = "http://localhost:8800") -> str:
    """
    Call the Jenny Agent API with a prompt
    
    Args:
        prompt: The question or prompt to send to Jenny
        base_url: The base URL of the API (default: http://localhost:8800)
        
    Returns:
        The response from Jenny
    """
    url = f"{base_url}/jenny"
    
    try:
        response = requests.post(
            url,
            json={"prompt": prompt},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        
        result = response.json()
        return result["response"]
    
    except requests.exceptions.ConnectionError:
        return "❌ Error: Could not connect to API. Is the server running?"
    except requests.exceptions.HTTPError as e:
        return f"❌ HTTP Error: {e}"
    except Exception as e:
        return f"❌ Error: {e}"


def check_health(base_url: str = "http://localhost:8800") -> bool:
    """Check if the API is healthy"""
    try:
        response = requests.get(f"{base_url}/health")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def main():
    base_url = "http://localhost:8800"
    
    print("🔍 Checking API health...")
    if not check_health(base_url):
        print("❌ API is not running!")
        print("\nPlease start the API server first:")
        print("  cd agents")
        print("  uvicorn jenny_api:app --host 0.0.0.0 --port 8800")
        return
    
    print("✅ API is healthy!\n")
    
    # Example 1: Single question
    print("Example 1: Single API Call")
    print("-" * 50)
    prompt = "Explain what a REST API is in one sentence."
    print(f"Prompt: {prompt}")
    response = call_jenny_api(prompt, base_url)
    print(f"Response: {response}\n")
    
    # Example 2: Multiple questions
    print("\nExample 2: Multiple API Calls")
    print("-" * 50)
    
    prompts = [
        "What is the difference between PUT and PATCH?",
        "What is idempotency in REST APIs?",
        "What are HTTP status codes used for?"
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n{i}. Prompt: {prompt}")
        response = call_jenny_api(prompt, base_url)
        print(f"   Response: {response}")
    
    print("\n✅ Done! All API calls completed.")


if __name__ == "__main__":
    main()
