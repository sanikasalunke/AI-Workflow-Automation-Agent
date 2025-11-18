from typing import Dict
import json

def planning_prompt(user_input):
    return f"""You are an automation planner. Break down the user's request into a JSON list of steps.
User request: {user_input}

Output ONLY valid JSON in this format:
{{"steps":[{{"tool":"tool_name","input": "string or object"}}]}}
"""

class Planner:
    def __init__(self, llm):
        self.llm = llm

    def plan(self, user_input: str) -> Dict:
        prompt = planning_prompt(user_input)
        raw = self.llm.generate_text(prompt, max_tokens=512)
        # Attempt safe extraction - many LLMs will return JSON directly but might add text.
        start = raw.find("{")
        if start != -1:
            raw = raw[start:]
        try:
            plan = json.loads(raw)
        except Exception:
            # fallback: naive single-step plan
            plan = {"steps": [{"tool": "read_file", "input": "README.md"}]}
        return plan
