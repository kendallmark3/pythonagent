"""
Jenny Agent REST API
Step 2: Expose the agent as a REST API using FastAPI

This module provides an HTTP interface to the Jenny agent,
allowing it to be invoked by other services, CI/CD pipelines,
automation tools, or any HTTP client.
"""

import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Add the agents directory to the path so we can import jenny
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jenny import JennyAgent

app = FastAPI(
    title="Jenny Agent API",
    description="A Python-based AI agent exposed as a REST API",
    version="1.0.0"
)

# Request/Response models
class JennyRequest(BaseModel):
    """Request model for Jenny agent invocation"""
    prompt: str

class JennyResponse(BaseModel):
    """Response model from Jenny agent"""
    response: str

# Initialize the agent lazily
_agent = None

def get_agent():
    """Get or create the Jenny agent instance"""
    global _agent
    if _agent is None:
        try:
            _agent = JennyAgent()
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to initialize Jenny agent: {str(e)}"
            )
    return _agent

@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "service": "Jenny Agent API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/jenny", response_model=JennyResponse)
def call_jenny(req: JennyRequest):
    """
    Call the Jenny agent with a prompt
    
    Args:
        req: JennyRequest containing the prompt
        
    Returns:
        JennyResponse containing the agent's response
    """
    agent = get_agent()
    result = agent.run(req.prompt)
    return JennyResponse(response=result)
