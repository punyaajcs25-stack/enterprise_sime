# Enterprise SIEM Simulation

A local, educational SIEM-style project. It generates synthetic enterprise events,
normalises and stores them in SQLite, correlates events, detects selected patterns,
and provides a Streamlit dashboard.

## Requirements
- Python 3.10+
- macOS, Windows, or Linux

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
```

## Run the simulation
```bash
python main.py
```

## Open the dashboard
```bash
streamlit run dashboard/app.py
```

## Run tests
```bash
python -m pytest -q
```

All events are synthetic. This project does not monitor real devices or perform
real attacks. It is intended for learning and demonstration.
