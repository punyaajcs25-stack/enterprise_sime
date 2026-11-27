import json
from .event_schema import normalise_event

def collect_events(events, path):
    accepted = []
    rejected = 0
    with open(path, "w", encoding="utf-8") as handle:
        for raw in events:
            try:
                event = normalise_event(raw)
                handle.write(json.dumps(event) + "\\n")
                accepted.append(event)
            except (TypeError, ValueError):
                rejected += 1
    return accepted, rejected
