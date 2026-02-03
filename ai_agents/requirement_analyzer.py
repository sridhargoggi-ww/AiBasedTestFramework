import openai
from pydantic import BaseModel

class Requirement(BaseModel):
    id: str
    title: str
    description: str
    acceptance_criteria: list[str]

class RequirementAnalyzer:

    def analyze(self, requirement_text):
        prompt = f"""
        Extract testable requirements and acceptance criteria:
        {requirement_text}
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
