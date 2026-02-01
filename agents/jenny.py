import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class JennyAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.system_prompt = (
            "You are Jenny, a helpful engineering assistant. "
            "You reason step-by-step and give concise, practical answers."
        )

    def run(self, user_input: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    print("🤖 Jenny Agent started. Type 'exit' to quit.\n")
    agent = JennyAgent()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            print("👋 Jenny signing off.")
            break
        reply = agent.run(user_input)
        print(f"\nJenny: {reply}\n")
