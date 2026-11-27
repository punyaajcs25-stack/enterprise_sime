import random
from datetime import datetime, timedelta, timezone

DEPARTMENTS = ["HR", "Finance", "IT", "Admin"]
USERS = {"HR": ["maya", "arun"], "Finance": ["riya", "dev"],
         "IT": ["sam", "noah"], "Admin": ["alex", "lee"]}

def generate_events(count=60, seed=7):
    rng = random.Random(seed)
    events = []
    start = datetime.now(timezone.utc) - timedelta(minutes=30)
    for i in range(count):
        dept = rng.choice(DEPARTMENTS)
        user = rng.choice(USERS[dept])
        suspicious = i % 13 in (0, 1, 2, 3, 4)
        event_type = "login"
        status = "failure" if suspicious else rng.choice(["success", "success", "failure"])
        ip = "203.0.113.25" if suspicious else f"10.0.{rng.randint(1, 4)}.{rng.randint(10, 240)}"
        details = "Synthetic authentication event"
        if i % 17 == 0:
            event_type, status, details = "privilege_change", "success", "Role or permission changed"
        elif i % 11 == 0:
            event_type, status, details = "file_access", "success", "Accessed payroll.csv"
        events.append({
            "timestamp": (start + timedelta(seconds=i * 20)).isoformat(),
            "department": dept, "username": user, "source_ip": ip,
            "event_type": event_type, "status": status, "details": details
        })
    return events
