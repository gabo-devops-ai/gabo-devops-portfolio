# Vertex AI MLOps Lab

**Objective**
- Provision Vertex AI resources with Terraform.
- Train and deploy a simple ML model (e.g., sklearn).
- Integrate CI/CD with GitHub Actions.

## Diagram
```mermaid
flowchart LR
  code[GitHub Actions] --> tf[Terraform: Vertex AI + GCS]
  tf --> job[Vertex AI Training Job]
  job --> model[Deployed Model Endpoint]

