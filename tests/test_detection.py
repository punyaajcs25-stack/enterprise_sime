from siem.detection import detect_threats

def make_event(i, status="failure", ip="198.51.100.10", user="tester"):
    return {"timestamp": f"2026-01-01T00:00:{i:02d}+00:00",
            "department": "IT", "username": user, "source_ip": ip,
            "event_type": "login", "status": status, "details": ""}

def test_detects_brute_force():
    events = [make_event(i) for i in range(5)]
    incidents = detect_threats(events)
    assert any("brute-force" in item["title"] for item in incidents)

def test_does_not_flag_below_threshold():
    incidents = detect_threats([make_event(i) for i in range(4)])
    assert not any("brute-force" in item["title"] for item in incidents)

def test_detects_privilege_change():
    event = make_event(1, status="success")
    event["event_type"] = "privilege_change"
    incidents = detect_threats([event])
    assert any("Privilege change" in item["title"] for item in incidents)
