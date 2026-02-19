# AiBasedTestFramework
A test framework that helps analyze, create and run tests based on User stories using free, open-source LLMs (powered by gpt4all).

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- ~4GB free disk space (for gpt4all model download on first run)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/sridhargoggi-ww/AiBasedTestFramework.git
cd AiBasedTestFramework
```

2. **Create a Python virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure Jira credentials:**
   - Copy `.env.example` to `.env`
   - Edit `.env` and add your Jira credentials:
     ```bash
     JIRA_URL=https://yourcompany.atlassian.net
     JIRA_EMAIL=your-email@company.com
     JIRA_API_TOKEN=<get-from-jira-account-settings>
     JIRA_PROJECT=YOUR_PROJECT_KEY
     ```
   - **⚠️ Important:** `.env` is in `.gitignore` and will never be committed
   - Get your API token: Jira → Account Settings → Security → API tokens

5. **Run the test generation agent:**
```bash
python run_agent.py
```

The agent will:
- Fetch requirements from Jira using your credentials
- Use gpt4all (local LLM) to extract acceptance criteria
- Generate manual and automation test cases
- Save artifacts to `test_artifacts/`

### To use with Azure DevOps instead:
Add these environment variables to your `.env` file:
```bash
ADO_ORG_URL=https://dev.azure.com/your-org
ADO_PROJECT=YourProject
ADO_PAT=<your-personal-access-token>
```

## 📁 Project Structure

```
├── ai_agents/              # AI agent implementations
│   ├── requirement_analyzer.py   # Uses gpt4all to analyze requirements
│   ├── test_generator.py         # Generates test code
│   └── change_detector.py
├── test_artifacts/         # Generated test artifacts
│   ├── automation/        # Automated test scripts (Python/Playwright)
│   └── manual/           # Manual test documentation (JSON)
├── framework/            # UI testing framework
├── integrations/         # Jira/ADO integrations (optional)
├── metrics/             # Test coverage metrics
├── config.py           # Configuration settings
└── run_agent.py       # Main entry point
```

## 🎯 Features

✅ **Free & No API Keys** - Uses gpt4all for local LLM inference  
✅ **Offline** - Works without internet after initial model download  
✅ **Automated Test Generation** - Analyzes requirements and generates test code  
✅ **Regression Tagging** - Tests are tagged as regression for CI/CD  
✅ **Playwright Integration** - Auto-generates browser automation scripts  

## � Security & Credentials

**IMPORTANT:** Never commit credentials to GitHub!

- ✅ Use `.env` file for local development (in `.gitignore`)
- ✅ Set environment variables in CI/CD pipelines
- ✅ Rotate API tokens regularly
- ✅ Use minimal permission API tokens

**Generating Jira API Token:**
1. Go to https://id.atlassian.com/manage/api-tokens
2. Click "Create API token"
3. Copy the token to your `.env` file
4. Never share or commit the token

## �🔧 Configuration

Edit `config.py` to customize:
- Test artifact path
- Browser headless mode
- LLM model selection

## 📝 Example Output

The agent generates:
- **Manual Test Cases**: Documented steps and expected results
- **Automation Scripts**: Playwright-based Python test code
- **Test Metadata**: JSON files with test IDs, criteria, and coverage info

## ⚙️ Technology Stack

- **LLM**: gpt4all (Mistral 7B)
- **Automation**: Playwright + Python
- **Validation**: Pydantic
- **Framework**: Custom Python-based test framework

## 📄 Note on venv/

The `venv/` folder is in `.gitignore` and **should not be committed**. When cloning this repo, you only need to:

```bash
python -m venv venv
pip install -r requirements.txt
```

This creates a fresh virtual environment with all required dependencies.
