# Infra as Code on AWS (Terraform)

Minimal AWS baseline using Terraform modules:
- VPC (public/private subnets)
- EC2 (sample web server)
- RDS (PostgreSQL)
- S3 (artifact/log bucket)

## Quickstart
1. Install Terraform >= 1.6
2. Export AWS credentials (use a test account):
   ```bash
   export AWS_REGION=us-east-1
   export AWS_PROFILE=default
   ```
3. Initialize and apply:
   ```bash
   terraform init
   terraform apply -auto-approve
   ```
4. Destroy when done:
   ```bash
   terraform destroy -auto-approve
   ```

> For demo only. Replace placeholder values. Never commit real secrets.