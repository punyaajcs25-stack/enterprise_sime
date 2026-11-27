from datetime import datetime, timezone
from uuid import uuid4

REQUIRED_FIELDS = {"timestamp", "department", "username", "source_ip", "event_type", "status"}

def normalise_event(raw: dict) -> dict:
    missing = REQUIRED_FIELDS - raw.keys()
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(sorted(missing))}")
    event = dict(raw)
    event["event_id"] = str(raw.get("event_id") or uuid4())
    event["timestamp"] = str(raw["timestamp"])
    event["department"] = str(raw["department"]).strip()
    event["username"] = str(raw["username"]).strip()
    event["source_ip"] = str(raw["source_ip"]).strip()
    event["event_type"] = str(raw["event_type"]).strip().lower()
    event["status"] = str(raw["status"]).strip().lower()
    event["details"] = str(raw.get("details", ""))
    return event

def utc_now():
    return datetime.now(timezone.utc).isoformat()
