# AIOps Log Analyzer (Prototype)

I sometimes use a quick statistical pass to spot "did something blow up?" moments.
This script flags spikes in error rates using a rolling Z-score. It's not production-grade ML,
but it's a practical starting point for alert tuning and postmortems.

How I'd extend this:
- Persist metrics to a TSDB and visualize in Grafana.
- Use more robust detectors (EWMA, STL, seasonality-aware models).
- Feed results back into incident response (PagerDuty/Slack).
