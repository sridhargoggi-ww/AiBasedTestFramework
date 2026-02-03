import requests

class JiraClient:
    def __init__(self, base_url, email, api_token, project_key):
        self.base_url = base_url
        self.auth = (email, api_token)
        self.project_key = project_key

    def get_stories(self, max_results=5):
        url = f"{self.base_url}/rest/api/2/search"
        query = {
            "jql": f"project={self.project_key} AND issuetype=Story ORDER BY created DESC",
            "maxResults": max_results
        }
        response = requests.get(url, auth=self.auth, params=query)
        response.raise_for_status()
        issues = response.json()["issues"]
        return [
            {
                "id": i["id"],
                "key": i["key"],
                "summary": i["fields"]["summary"],
                "description": i["fields"]["description"]
            } for i in issues
        ]
