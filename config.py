import os
import sys

# ===== JIRA CONFIGURATION =====
# Set these via environment variables (see .env.example)
JIRA_URL = os.environ.get("JIRA_URL")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")
JIRA_PROJECT = os.environ.get("JIRA_PROJECT")

# Validate required Jira configuration
if not all([JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT]):
    print("❌ ERROR: Missing required Jira configuration!")
    print("Set these environment variables:")
    print("  - JIRA_URL (e.g., https://yourcompany.atlassian.net)")
    print("  - JIRA_EMAIL (e.g., user@company.com)")
    print("  - JIRA_API_TOKEN (generate from Jira Account Settings)")
    print("  - JIRA_PROJECT (e.g., PROJ)")
    print("\nSee .env.example for reference")
    sys.exit(1)

# ===== AZURE DEVOPS CONFIGURATION =====
# Set these via environment variables (optional, if using ADO)
ADO_ORG_URL = os.environ.get("ADO_ORG_URL")
ADO_PROJECT = os.environ.get("ADO_PROJECT")
ADO_PAT = os.environ.get("ADO_PAT")

# Test artifact path
TEST_ARTIFACT_PATH = "test_artifacts/"

# Browser config
HEADLESS = False

# GPT4All LLM Model (free, no API keys required)
# Model will be automatically downloaded on first run
LLM_MODEL = "mistral-7b-instruct-v0.1.Q4_0.gguf"
