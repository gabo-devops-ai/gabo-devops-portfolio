# Azure OpenAI Incident Helper (KQL generator)

Goal: Given an incident context (service, region, symptom), propose Kusto queries for Azure Log Analytics and a short diagnostic checklist.

Env:
- AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY
- AZURE_OPENAI_DEPLOYMENT (e.g., gpt-4o-mini)
