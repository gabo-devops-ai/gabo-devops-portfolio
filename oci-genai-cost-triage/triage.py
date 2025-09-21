import json

PROMPT_TMPL = """You are a cloud FinOps helper for OCI.
Given this cost JSON (truncated), suggest the top 5 likely causes of the spike and a 6-step action plan.
Focus on: OKE nodes, block storage snapshots, S3-compatible requests, data egress, NAT gateways, LB tiers.

COST JSON:
{body}
"""

def summarize_cost(cost_rows):
    # This is where I'd call OCI Generative AI (commented for demo)
    # For now, return a deterministic demo summary.
    return {
        "likely_causes": [
            "OKE node pool scale-out (missing autoscaler limits).",
            "Block storage snapshots left running.",
            "High S3-compatible GET/PUT requests on a public bucket.",
            "Unrestricted egress via NAT gateway.",
            "Load balancer moved to higher tier."
        ],
        "action_plan": [
            "Tag and cap node pools; review HPA/VPA.",
            "Prune snapshots; enforce retention.",
            "Enable lifecycle rules and restrict bucket access.",
            "Add egress alerts; review NAT traffic.",
            "Downshift LB tier if feasible.",
            "Set budgets + anomaly alerts."
        ]
    }

if __name__ == "__main__":
    sample = {"items":[{"service":"OKE","cost":320.5},{"service":"LB","cost":88.1}]}
    print(json.dumps(summarize_cost(sample), indent=2))
