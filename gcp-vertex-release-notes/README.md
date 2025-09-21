# GCP Vertex AI – Release Notes Generator (Cloud Run)

Goal: Turn commit/PR metadata into human-friendly release notes + a technical changelog.
Deploy on Cloud Run, call Vertex AI for summarization (activate later).

Env:
- GOOGLE_CLOUD_PROJECT
- LOCATION (e.g., us-central1)
- MODEL (e.g., text-unicorn@001)
