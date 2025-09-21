import json, os

SYSTEM = "You are a pragmatic SRE assistant on Azure."
USER_TMPL = """Service: {service}
Region: {region}
Symptom: {symptom}

1) Propose 3 KQL queries for Azure Log Analytics to triage quickly.
2) Provide a short checklist (5-8 bullets) with likely causes and next steps.
Keep it concise and directly runnable.
"""

def generate_payload(service, region, symptom):
    user = USER_TMPL.format(service=service, region=region, symptom=symptom)
    return {"role":"user","content":user}

def main():
    # --- Azure OpenAI call (commented) ---
    # import requests
    # endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    # key = os.getenv("AZURE_OPENAI_KEY")
    # deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT","gpt-4o-mini")
    # resp = requests.post(
    #   f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-02-15-preview",
    #   headers={"api-key": key, "Content-Type":"application/json"},
    #   data=json.dumps({"messages":[{"role":"system","content":SYSTEM}, generate_payload("payments-api","eastus","p95 latency up")], "temperature":0.2})
    # )
    # print(resp.json())

    # Demo output
    print(json.dumps({
        "kql": [
            "requests | where cloud_RoleName == 'payments-api' and resultCode !in ('200','204') | summarize count() by resultCode, bin(timestamp, 5m)",
            "traces | where message contains 'timeout' | summarize count() by bin(timestamp, 5m)",
            "performanceCounters | where name == 'cpuUsage' | summarize avg(value) by bin(timestamp, 1m)"
        ],
        "checklist": [
            "Check upstream dependency timeouts (db, redis).",
            "Look for 429/5xx spikes around deploy window.",
            "Verify thread pool saturation.",
            "Compare p95 vs. p50 to spot outliers.",
            "Roll back last change if error budget breached."
        ]
    }, indent=2))

if __name__ == "__main__":
    main()
