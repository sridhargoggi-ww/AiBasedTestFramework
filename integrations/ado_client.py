import requests

class AdoClient:
    def __init__(self, org_url, project, pat):
        self.base_url = f"{org_url}/{project}/_apis/wit/workitems"
        self.headers = {"Authorization": f"Basic {pat}"}

    def get_work_items(self, ids):
        ids_str = ",".join(map(str, ids))
        url = f"{self.base_url}?ids={ids_str}&api-version=7.0"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()["value"]
