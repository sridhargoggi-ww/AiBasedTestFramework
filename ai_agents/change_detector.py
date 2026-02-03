import json
from pathlib import Path

class ChangeDetector:
    """
    Detects changes in requirements compared to previous versions.
    """

    def __init__(self, artifact_path="test_artifacts/manual"):
        self.artifact_path = Path(artifact_path)

    def has_changed(self, req_id, new_description):
        """
        Checks if a requirement has changed compared to the previous artifact.
        """
        file_path = self.artifact_path / f"{req_id}.json"
        if not file_path.exists():
            # No previous artifact, treat as new
            return True

        old_data = json.load(open(file_path))
        old_description = old_data.get("description", "")

        return old_description.strip() != new_description.strip()

    def list_changed_requirements(self, requirements):
        """
        Returns a list of requirement IDs that have changed.
        """
        changed = []
        for req in requirements:
            if self.has_changed(req["key"], req["description"]):
                changed.append(req)
        return changed
