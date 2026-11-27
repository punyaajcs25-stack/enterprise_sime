from config import LOG_PATH
from .generator import generate_events
from .collector import collect_events
from .storage import save_events, save_incidents
from .detection import detect_threats
from .correlation import correlate_events

def run_pipeline(count=60, seed=7):
    generated = generate_events(count=count, seed=seed)
    events, rejected = collect_events(generated, LOG_PATH)
    save_events(events)
    incidents = detect_threats(events)
    save_incidents(incidents)
    correlations = correlate_events(events)
    return {"generated": len(generated), "accepted": len(events),
            "rejected": rejected, "incidents": incidents,
            "correlations": correlations}
