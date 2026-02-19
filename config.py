import os

# Jira / Azure DevOps
# Load from environment variables (set via .env file or system env)
JIRA_URL = os.environ.get("JIRA_URL", "https://sridhargoggi.atlassian.net")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL", "sridhargoggi@gmail.com")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")  # From .env file
JIRA_PROJECT = os.environ.get("JIRA_PROJECT", "MyTestJira")

ADO_ORG_URL = "https://dev.azure.com/your-org"
ADO_PROJECT = "DemoProject"
ADO_PAT = "your-azure-devops-pat"

# Test artifact path
TEST_ARTIFACT_PATH = "test_artifacts/"

# Browser config
HEADLESS = False

# GPT4All LLM Model (free, no API keys required)
# Model will be automatically downloaded on first run
LLM_MODEL = "mistral-7b-instruct-v0.1.Q4_0.gguf"
