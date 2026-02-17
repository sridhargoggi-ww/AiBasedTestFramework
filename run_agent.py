import os
import json
from integrations.jira_client import JiraClient
from ai_agents.requirement_analyzer import RequirementAnalyzer
from ai_agents.test_generator import generate_tests
from metrics.coverage import CoverageTracker
from config import *

# Initialize Jira Client
jira = JiraClient(JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT)

# Use demo requirement instead of fetching from Jira
USE_DEMO_REQUIREMENT = True

if USE_DEMO_REQUIREMENT:
    requirements = [{
        "key": "LOGIN_001",
        "summary": "User Login",
        "description": """
        As a user, I want to login.

        Acceptance Criteria:
        1. User can login with valid credentials
        2. Invalid login shows error to retry login or click forget password
        3. Successful login redirects to dashboard
        4. forget password redirects to reset password page
        5. User session persists after login
        6. Login page has 'Remember Me' option
        """
    }]
else:
    requirements = jira.get_stories()

analyzer = RequirementAnalyzer()
tracker = CoverageTracker(TEST_ARTIFACT_PATH)

for req in requirements:
    analysis = analyzer.analyze(req["description"])
    test_code = generate_tests(analysis)

    # Save manual artifact
    manual_path = os.path.join(TEST_ARTIFACT_PATH, "manual", f"{req['key']}.json")
    with open(manual_path, "w") as f:
        json.dump({
            "test_id": req["key"],
            "title": req["summary"],
            "description": req["description"],
            "ai_analysis": analysis,
            "test_code": test_code
        }, f, indent=2)

    # Save automation artifact
    automation_path = os.path.join(TEST_ARTIFACT_PATH, "automation", f"{req['key']}.py")
    with open(automation_path, "w") as f:
        f.write(test_code)

# Print coverage report
coverage = tracker.calculate_coverage()
print("Coverage Metrics:", coverage)
