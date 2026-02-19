import os
import json
from integrations.jira_client import JiraClient
from ai_agents.requirement_analyzer import RequirementAnalyzer
from ai_agents.test_generator import generate_tests
from metrics.coverage import CoverageTracker
from config import *

# Initialize Jira Client
jira = JiraClient(JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT)

# Fetch requirements from Jira
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
