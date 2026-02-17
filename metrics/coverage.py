import json
from pathlib import Path

class CoverageTracker:
    def __init__(self, artifact_path="test_artifacts/"):
        self.artifact_path = Path(artifact_path)

    def calculate_coverage(self):
        manual = list((self.artifact_path / "manual").glob("*.json"))
        automation = list((self.artifact_path / "automation").glob("*.py"))
        total = len(manual)
        automated = len(automation)
        functional_coverage = round((automated/total)*100 if total else 0, 2)
        return {
            "total_tests": total,
            "automated_tests": automated,
            "functional_coverage": f"{functional_coverage}%",
            "high_risk_covered": f"{self.high_risk_coverage()}%"
        }

    def high_risk_coverage(self):
        high_risk_manual = 0
        high_risk_automation = 0
        for f in (self.artifact_path / "manual").glob("*.json"):
            try:
                with open(f) as file:
                    data = json.load(file)
                    if data.get("risk") == "High":
                        high_risk_manual += 1
            except (json.JSONDecodeError, ValueError):
                # Skip invalid or empty JSON files
                pass
        for f in (self.artifact_path / "automation").glob("*.py"):
            if "LOGIN" in f.name:  # demo heuristic
                high_risk_automation += 1
        return round((high_risk_automation / high_risk_manual * 100) if high_risk_manual else 0, 2)
