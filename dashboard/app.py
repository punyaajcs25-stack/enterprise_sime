import streamlit as st
import pandas as pd
import plotly.express as px
from siem.storage import fetch_events, fetch_incidents
from siem.pipeline import run_pipeline
from siem.reports import export_incidents

st.set_page_config(page_title="Enterprise SIEM", layout="wide")
st.title("Enterprise SIEM Monitoring Dashboard")
st.caption("Educational simulation using synthetic enterprise security events.")

if st.button("Run new simulation"):
    result = run_pipeline()
    st.success(f"Processed {result['accepted']} events and created {len(result['incidents'])} incident records.")

events = pd.DataFrame(fetch_events())
incidents = pd.DataFrame(fetch_incidents())

c1, c2, c3 = st.columns(3)
c1.metric("Stored events", len(events))
c2.metric("Incident records", len(incidents))
c3.metric("High severity", int((incidents["severity"] == "High").sum()) if not incidents.empty else 0)

if not events.empty:
    st.subheader("Events by department")
    st.plotly_chart(px.histogram(events, x="department", color="event_type"), use_container_width=True)
    st.subheader("Recent events")
    st.dataframe(events, use_container_width=True)
else:
    st.info("No events yet. Run `python main.py` or click the simulation button.")

st.subheader("Security incidents")
if not incidents.empty:
    st.plotly_chart(px.histogram(incidents, x="severity", color="severity"), use_container_width=True)
    st.dataframe(incidents, use_container_width=True)
    if st.button("Export incident CSV"):
        path = export_incidents(incidents.to_dict("records"))
        st.success(f"Report saved to {path}")
else:
    st.write("No incidents recorded yet.")
