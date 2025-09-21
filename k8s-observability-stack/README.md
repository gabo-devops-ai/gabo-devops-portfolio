# Kubernetes Observability Stack (Demo)

This is the bare minimum I use to validate Prometheus + Grafana on a cluster.
It's intentionally small so people can read it end-to-end before we jump to Helm charts.

## What this demo does
- Creates an "observability" namespace.
- Deploys Prometheus and Grafana with in-cluster services.
- Uses emptyDir (fast and disposable) for lab storage.

## What I'd change for production
- Use Helm charts with sane defaults and overrides (values.yaml).
- Add PersistentVolumes for Prometheus/Grafana data.
- Secure Grafana admin via K8s Secret and network policies.
- Add dashboards and alerts (latency, error rates, saturation, SLOs).

## Apply (lab only)
kubectl apply -f namespace.yaml
kubectl apply -f prometheus/
kubectl apply -f grafana/

## Port-forward quick check
kubectl -n observability port-forward svc/grafana 3000:3000
open http://localhost:3000

Note: this is a lab. For a real setup I'd wire this to an Ingress and auth.
