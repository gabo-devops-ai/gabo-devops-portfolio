# 🚀 Real-World DevOps & SRE Portfolio – Gabriel Gonzalez ♐

[![CI](https://github.com/gabo-devops-ai/gabo-devops-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/gabo-devops-ai/gabo-devops-portfolio/actions)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---
[![Forks][forks-shield]][forks-url]
[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Last Commit][commit-shield]][commit-url]
[![Code of Conduct][coc-shield]][coc-url]
[![Contributing][contrib-shield]][contrib-url]
<!-- MARKDOWN LINKS & IMAGES -->

[forks-shield]: https://img.shields.io/github/forks/gabo-devops-ai/gabo-devops-portfolio?style=for-the-badge&logo=github&logoColor=white&color=orange
[forks-url]: https://github.com/gabo-devops-ai/gabo-devops-portfolio/network/members

[stars-shield]: https://img.shields.io/github/stars/gabo-devops-ai/gabo-devops-portfolio.svg?style=for-the-badge&logo=github&logoColor=white&color=brightgreen
[stars-url]: https://github.com/gabo-devops-ai/gabo-devops-portfolio/stargazers

[issues-shield]: https://img.shields.io/github/issues/gabo-devops-ai/gabo-devops-portfolio?style=for-the-badge&logo=github&logoColor=white&color=blue
[issues-url]: https://github.com/gabo-devops-ai/gabo-devops-portfolio/issues

[commit-shield]: https://img.shields.io/github/last-commit/gabo-devops-ai/gabo-devops-portfolio?style=for-the-badge&logo=git&logoColor=white&color=ff69b4
[commit-url]: https://github.com/gabo-devops-ai/gabo-devops-portfolio/commits/save

[coc-shield]: https://img.shields.io/badge/Code%20of%20Conduct-Enforced-blueviolet?style=for-the-badge&logo=handshake&logoColor=white
[coc-url]: https://github.com/gabo-devops-ai/gabo-devops-portfolio/blob/master/CODE_OF_CONDUCT.md

[contrib-shield]: https://img.shields.io/badge/Contributions-Welcome-ff69b4?style=for-the-badge&logo=gitbook&logoColor=white
[contrib-url]: https://github.com/gabo-devops-ai/gabo-devops-portfolio/blob/master/CONTRIBUTING.md


![DevOps-Portfolio](https://divinosoft.ca/portfolio-devops.png)
---

## 🎯 Purpose of Portfolio

This portfolio demonstrates **real-world DevOps & SRE skills** across multi-cloud environments:  
- Infrastructure as Code (IaC) with Terraform, Ansible, and Pulumi.  
- CI/CD pipelines using GitHub Actions and GitLab CI.  
- Kubernetes and observability stacks with Prometheus, Grafana, and CloudWatch.  
- AI-driven automation for log analysis, incident management, and FinOps.  

The goal is to show practical, annotated projects that reflect **how I solve problems in production** rather than just “perfect lab demos.”

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

## 📚 Labs by Level

### 🟢 Foundation
- [infra-as-code-aws/](infra-as-code-aws/) – Terraform S3 bucket module  
- [ci-cd-pipeline-demo/](ci-cd-pipeline-demo/) – Python app + GitHub Actions pipeline  

### 🟡 Intermediate
- [k8s-observability-stack/](k8s-observability-stack/) – Prometheus + Grafana on Kubernetes  
- [oci-genai-cost-triage/](oci-genai-cost-triage/) – OCI cost triage with GenAI  

### 🔴 Advanced
- [aiops-log-analyzer/](aiops-log-analyzer/) – Log anomaly detection with optional AI  
- [aws-bedrock-incident-summarizer/](aws-bedrock-incident-summarizer/) – AWS Bedrock incident summarization  
- [gcp-vertex-release-notes/](gcp-vertex-release-notes/) – GCP Vertex AI release notes generator  
- [azure-openai-incident-helper/](azure-openai-incident-helper/) – Azure OpenAI KQL + incident helper  

---

## 🛠️ Tech Stack

| Cloud | IaC & Config | Containers & Orchestration | CI/CD & SCM | Monitoring & AI |
|-------|--------------|-----------------------------|--------------|-----------------|
| ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) | ![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white) | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white) | ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white) |
| ![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white) | ![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white) | ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) | ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white) |
| ![GCP](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white) | ![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white) | ![Minikube](https://img.shields.io/badge/Minikube-00ADD8?style=for-the-badge&logo=kubernetes&logoColor=white) | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) | ![AI/ML](https://img.shields.io/badge/AI%2FML-BB4CFC?style=for-the-badge&logo=OpenAI&logoColor=white) |
| ![OCI](https://img.shields.io/badge/Oracle_Cloud-F80000?style=for-the-badge&logo=oracle&logoColor=white) | ![Pulumi](https://img.shields.io/badge/Pulumi-512BD4?style=for-the-badge&logo=pulumi&logoColor=white) | ![Kind](https://img.shields.io/badge/Kind-FFD700?style=for-the-badge&logo=kubernetes&logoColor=black) | ![GitLab](https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white) | ![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=for-the-badge&logo=amazon-cloudwatch&logoColor=white) |

---

## 🚀 Quickstart

Clone the repo and explore the labs:

```bash
git clone https://github.com/gabo-devops-ai/gabo-devops-portfolio.git
cd gabo-devops-portfolio
```

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=gabo-devops-ai/gabo-devops-portfolio&type=Date)](https://www.star-history.com/#gabo-devops-ai/gabo-devops-portfolio&Date)

---

## 📬 Contact / About Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/gabriel-gonzalez-montero)  
[![GitHub](https://img.shields.io/badge/GitHub-gabo--devops--ai-black?logo=github)](https://github.com/gabo-devops-ai)  
[![Email](https://img.shields.io/badge/Email-gabo.1985@gmail.com-red?logo=gmail&logoColor=white)](mailto:gabo.1985@gmail.com)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  

---

## 🌍 Repo Insights

<p align="center">
  <img src="https://img.shields.io/github/stars/gabo-devops-ai/gabo-devops-portfolio?style=social" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/gabo-devops-ai/gabo-devops-portfolio?style=social" alt="GitHub forks"/>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=gabo-devops-ai.gabo-devops-portfolio" alt="Visitors"/>
</p>

---

## 📊 GitHub Stats & Languages

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=gabo-devops-ai&show_icons=true&theme=tokyonight" alt="GitHub stats"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=gabo-devops-ai&layout=compact&theme=tokyonight" alt="Top Langs"/>
</p>

---

## 🤝 Contribute & Collaborate

Contributions, suggestions, and improvements are always welcome!  
If you’d like to collaborate or discuss DevOps, SRE, and AI-driven automation, feel free to connect with me via [LinkedIn](https://www.linkedin.com/in/gabriel-gonzalez-montero).

