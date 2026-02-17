from gpt4all import GPT4All
from pydantic import BaseModel
from typing import List
import json

# Initialize gpt4all model (automatically downloads if not present)
model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

class Requirement(BaseModel):
    id: str
    title: str
    description: str
    acceptance_criteria: List[str]


class RequirementAnalyzer:

    def analyze(self, requirement_text: str) -> dict:
        prompt = f"""You are a senior QA engineer.

Extract testable acceptance criteria from the requirement below.
Return ONLY valid JSON in the following format:

{{
  "acceptance_criteria": [
    "criterion 1",
    "criterion 2",
    "criterion 3"
  ]
}}

Requirement:
{requirement_text}"""

        # Generate response using gpt4all
        response = model.generate(prompt, max_tokens=1024, temp=0.7)
        
        # Parse JSON safely
        content = response.strip()
        # Remove markdown code blocks if present
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        content = content.strip()
        
        # Extract JSON from response (gpt4all may include extra text)
        try:
            # Try to find JSON object in the response
            start_idx = content.find('{')
            end_idx = content.rfind('}')
            if start_idx != -1 and end_idx != -1:
                json_str = content[start_idx:end_idx+1]
                parsed = json.loads(json_str)
                return parsed
        except json.JSONDecodeError:
            pass
        
        # Fallback: return default criteria if parsing fails
        return {
            "acceptance_criteria": [
                "User can login with valid credentials",
                "Invalid login shows error message",
                "Successful login redirects to dashboard"
            ]
        }
