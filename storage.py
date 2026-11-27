import sqlite3
from config import DB_PATH

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialise():
    with connect() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY, timestamp TEXT, department TEXT,
            username TEXT, source_ip TEXT, event_type TEXT, status TEXT, details TEXT
        )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS incidents (
            incident_id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT,
            title TEXT, severity TEXT, source_ip TEXT, username TEXT,
            description TEXT, status TEXT DEFAULT 'Open'
        )''')

def save_events(events):
    initialise()
    with connect() as conn:
        for e in events:
            conn.execute('''INSERT OR IGNORE INTO events VALUES
                (?, ?, ?, ?, ?, ?, ?, ?)''',
                tuple(e.get(k, "") for k in ["event_id","timestamp","department","username",
                    "source_ip","event_type","status","details"]))

def save_incidents(incidents):
    initialise()
    with connect() as conn:
        for i in incidents:
            conn.execute('''INSERT INTO incidents
                (timestamp,title,severity,source_ip,username,description,status)
                VALUES (?,?,?,?,?,?,?)''',
                (i["timestamp"], i["title"], i["severity"], i["source_ip"],
                 i["username"], i["description"], "Open"))

def fetch_events():
    initialise()
    with connect() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM events ORDER BY timestamp DESC")]

def fetch_incidents():
    initialise()
    with connect() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM incidents ORDER BY incident_id DESC")]
