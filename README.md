# DevOps & SRE Portfolio – Gabriel Gonzalez Montero

[![CI](https://github.com/gabo-devops-ai/gabo-devops-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/gabo-devops-ai/gabo-devops-portfolio/actions)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

This repository collects examples of how I approach multi-cloud DevOps, SRE practices, and AI-driven automation. Each folder is based on real scenarios I’ve worked on or prepared for, simplified for demo purposes but documented the way I would explain them to a teammate.

---

## 📂 Repository Structure

| Folder                          | Description                                  | AI Integration | Notes                                                                 |
|---------------------------------|----------------------------------------------|----------------|----------------------------------------------------------------------|
| infra-as-code-aws/              | Terraform module creating an S3 bucket       | No             | In production I’d add versioning, lifecycle rules, and remove force_destroy. |
| ci-cd-pipeline-demo/            | Python app with GitHub Actions pipeline      | No             | Real pipelines include staging/prod jobs, approvals, and caching.    |
| k8s-observability-stack/        | Prometheus + Grafana manifests for Kubernetes| No             | In production I’d deploy via Helm, with HA and persistent volumes.   |
| aiops-log-analyzer/             | Python script to detect error spikes in logs | Optional       | Can be extended with LLMs to generate summaries of anomalies.        |
| aws-bedrock-incident-summarizer/| CloudWatch Alarm → Lambda → Bedrock summary  | Yes            | Would connect to Slack/Teams, enforce IAM least privilege.           |
| gcp-vertex-release-notes/       | Cloud Run service: commit metadata → release notes | Yes        | Add authentication (IAP), service account scoping, and storage.     |
| azure-openai-incident-helper/   | Azure OpenAI tool to generate KQL + checklists| Yes           | Would wrap as a Function App, secure with KeyVault and RBAC.         |
| oci-genai-cost-triage/          | Parses OCI cost exports and suggests actions | Yes            | Plug into Budgets/Notifications, integrate with weekly FinOps.       |

---

## 🎯 Why this repo exists

- To demonstrate experience across AWS, GCP, Azure, and OCI.  
- To document patterns that I actually use in real projects, with notes on what I’d change in production.  
- To explore how AI can reduce operational toil: summarizing incidents, generating queries, and helping with cost triage.  
- To provide practical, annotated code that’s easier to learn from than “perfect” but abstract examples.  

---

## 🚀 Quickstart

Clone the repo and explore the labs:

```bash
git clone https://github.com/gabo-devops-ai/gabo-devops-portfolio.git
cd gabo-devops-portfolio
