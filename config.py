import os

# Jira / Azure DevOps
JIRA_URL = "https://your-domain.atlassian.net"
JIRA_EMAIL = "you@example.com"
JIRA_API_TOKEN = "your-jira-api-token"
JIRA_PROJECT = "DEMO"

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
