# DevOps & SRE Portfolio – Gabriel Gonzalez Montero

[![CI](https://github.com/gabo-devops-ai/gabo-devops-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/gabo-devops-ai/gabo-devops-portfolio/actions)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

This repository collects examples of how I approach multi-cloud DevOps, SRE practices, and AI-driven automation.  
Each folder is based on real scenarios I’ve worked on or prepared for, simplified for demo purposes but documented the way I would explain them to a teammate.

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

## 🛠️ Tech Stack

| Cloud | IaC & Config | Containers & Orchestration | CI/CD & SCM | Monitoring & AI |
|-------|--------------|-----------------------------|--------------|-----------------|
| ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) | ![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white) | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white) | ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white) |
| ![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white) | ![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white) | ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) | ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white) |
| ![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white) | ![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white) | ![Minikube](https://img.shields.io/badge/Minikube-00ADD8?style=for-the-badge&logo=kubernetes&logoColor=white) | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) | ![AI/ML](https://img.shields.io/badge/AI%2FML-BB4CFC?style=for-the-badge&logo=OpenAI&logoColor=white) |
| ![OCI](https://img.shields.io/badge/Oracle_Cloud-F80000?style=for-the-badge&logo=oracle&logoColor=white) | ![Pulumi](https://img.shields.io/badge/Pulumi-512BD4?style=for-the-badge&logo=pulumi&logoColor=white) | ![Kind](https://img.shields.io/badge/Kind-FFD700?style=for-the-badge&logo=kubernetes&logoColor=black) | ![GitLab](https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white) | ![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=for-the-badge&logo=amazon-cloudwatch&logoColor=white) |

---

## 📖 Labs

- [infra-as-code-aws/](infra-as-code-aws/) – Terraform S3 bucket module  
- [ci-cd-pipeline-demo/](ci-cd-pipeline-demo/) – Python app + GitHub Actions pipeline  
- [k8s-observability-stack/](k8s-observability-stack/) – Prometheus + Grafana on Kubernetes  
- [aiops-log-analyzer/](aiops-log-analyzer/) – Log anomaly detection with optional AI  
- [aws-bedrock-incident-summarizer/](aws-bedrock-incident-summarizer/) – AWS Bedrock incident summarization  
- [gcp-vertex-release-notes/](gcp-vertex-release-notes/) – GCP Vertex AI release notes generator  
- [azure-openai-incident-helper/](azure-openai-incident-helper/) – Azure OpenAI KQL + incident helper  
- [oci-genai-cost-triage/](oci-genai-cost-triage/) – OCI cost triage with GenAI  

---

## 🚀 Quickstart

Clone the repo and explore the labs:

```bash
git clone https://github.com/gabo-devops-ai/gabo-devops-portfolio.git
cd gabo-devops-portfolio
```

---


## 📬 Contact / About Me

- 🌐 [LinkedIn](https://www.linkedin.com/in/gabriel-gonzalez-montero)  
- 💻 [GitHub](https://github.com/gabo-devops-ai)  
- 📧 gabriel.1985cr@gmail.com  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  

---

## 🌍 Repo Insights

<p align="center">
  <img src="https://img.shields.io/github/stars/gabo-devops-ai/gabo-devops-portfolio?style=social" alt="GitHub stars" />
<img src="https://img.shields.io/github/forks/gabo-devops-ai/gabo-devops-portfolio?style=social" alt="GitHub forks" />
<img src="https://visitor-badge.laobi.icu/badge?page_id=gabo-devops-ai.gabo-devops-portfolio" alt="Visitors" />
</p>

---

## 📊 GitHub Stats & Languages

![Gabo's GitHub stats](https://github-readme-stats.vercel.app/api?username=gabo-devops-ai&show_icons=true&theme=tokyonight)  
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=gabo-devops-ai&layout=compact&theme=tokyonight)  

