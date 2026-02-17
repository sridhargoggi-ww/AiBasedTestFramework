from gpt4all import GPT4All

# Initialize gpt4all model (automatically downloads if not present)
model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

def generate_tests(requirement_analysis):
    prompt = f"""You are an expert QA automation engineer. Based on the following acceptance criteria, create:
    1. Manual test cases with detailed preconditions, steps, and expected results
    2. Automation-ready Playwright/Python test cases
    
    Acceptance Criteria:
    {requirement_analysis}
    
    Return test cases in a structured, formatted way."""

    # Generate response using gpt4all
    response = model.generate(prompt, max_tokens=2048, temp=0.7)
    return response
