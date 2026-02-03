def generate_tests(requirement_analysis):
    prompt = f"""
    Create:
    1. Manual test cases
    2. Automation-ready Playwright test cases
    Include:
    - Preconditions
    - Steps
    - Expected Results
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
