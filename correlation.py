from collections import defaultdict

def correlate_events(events, window_seconds=300):
    # Simple educational correlation: group failed logins by source IP.
    groups = defaultdict(list)
    for event in events:
        if event["event_type"] == "login" and event["status"] == "failure":
            groups[event["source_ip"]].append(event)
    return [
        {"source_ip": ip, "failed_attempts": len(items),
         "users": sorted({e["username"] for e in items})}
        for ip, items in groups.items() if len(items) >= 3
    ]
