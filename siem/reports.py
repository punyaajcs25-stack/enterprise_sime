import csv
from pathlib import Path

def export_incidents(incidents, output="reports/incidents.csv"):
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["timestamp", "title", "severity", "source_ip", "username", "description"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows([{k: item.get(k, "") for k in fields} for item in incidents])
    return path
