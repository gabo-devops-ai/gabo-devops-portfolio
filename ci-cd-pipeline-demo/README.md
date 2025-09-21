# CI/CD Pipeline Demo

GitHub Actions workflow that builds, tests, and publishes a Docker image for a simple Python app.
### Notes I leave for my future self / teammates
- I keep at least one quick unit test so CI doesn't become "build-only".
- The curl check is a tiny smoke test. In real services I'd use a readiness endpoint with retries/backoff.
- For prod I'd sign images and push to a private registry (ECR/GHCR), not Docker Hub.
