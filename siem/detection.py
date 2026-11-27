from collections import defaultdict
from datetime import datetime

def detect_threats(events, threshold=5):
    by_ip = defaultdict(list)
    for event in events:
        if event["event_type"] == "login" and event["status"] == "failure":
            by_ip[event["source_ip"]].append(event)
    incidents = []
    for ip, failures in by_ip.items():
        if len(failures) >= threshold:
            incidents.append({
                "timestamp": max(e["timestamp"] for e in failures),
                "title": "Possible brute-force activity",
                "severity": "High" if len(failures) >= threshold * 2 else "Medium",
                "source_ip": ip,
                "username": ", ".join(sorted({e["username"] for e in failures})),
                "description": f"{len(failures)} failed login attempts observed from {ip}."
            })
    for e in events:
        if e["event_type"] == "privilege_change":
            incidents.append({
                "timestamp": e["timestamp"], "title": "Privilege change observed",
                "severity": "Medium", "source_ip": e["source_ip"],
                "username": e["username"],
                "description": e.get("details", "Privilege change event")
            })
    return incidents
