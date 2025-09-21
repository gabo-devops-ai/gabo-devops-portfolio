terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# Simple S3 bucket for demo purposes.
# In real projects I've used a similar bucket for:
# - App logs (CloudWatch integration)
# - CI/CD build artifacts
# - Quick backups or CSV exports for analysts
#
# ⚠️ force_destroy is convenient for demos/labs.
#    In production I disable it to avoid accidental data loss.
resource "aws_s3_bucket" "artifacts" {
  bucket        = var.bucket_name
  force_destroy = true
}

output "bucket_name" {
  description = "Name of the created S3 bucket (useful to copy/paste elsewhere)."
  value       = aws_s3_bucket.artifacts.bucket
}
