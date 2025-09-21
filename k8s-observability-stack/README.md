# Kubernetes Observability Stack

Minimal manifests to deploy Prometheus and Grafana on a cluster.
For production, prefer Helm charts and persistent storage.

## Apply
```bash
kubectl apply -f namespace.yaml
kubectl apply -f prometheus/
kubectl apply -f grafana/
```