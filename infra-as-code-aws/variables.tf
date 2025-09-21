variable "region" {
  type        = string
  description = "AWS region"
  default     = "us-east-1"
}

variable "bucket_name" {
  type        = string
  description = "S3 bucket name (must be globally unique)"
  default     = "gabo-devops-portfolio-demo-bucket-CHANGE-ME"
}