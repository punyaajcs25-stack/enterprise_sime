from siem.pipeline import run_pipeline
from siem.reports import export_incidents

if __name__ == "__main__":
    result = run_pipeline()
    report = export_incidents(result["incidents"])
    print("Enterprise SIEM simulation complete")
    print(f"Generated: {result['generated']}")
    print(f"Accepted:  {result['accepted']}")
    print(f"Rejected:  {result['rejected']}")
    print(f"Correlations: {len(result['correlations'])}")
    print(f"Incidents: {len(result['incidents'])}")
    print(f"CSV report: {report}")
