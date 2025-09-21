import json, os, datetime
# from botocore.config import Config
# import boto3

def build_prompt(alarm):
    # Human-style prompt: short, concrete, action-biased.
    return f"""
You are an SRE on-call assistant.
Summarize this CloudWatch alarm in 8-10 lines: what's impacted, likely cause, quick checks, and next steps.
Alarm JSON:
{json.dumps(alarm)[:4000]}
"""

def handler(event, context):
    # Parse CloudWatch alarm/eventbridge input
    alarm = event.get("detail") or event
    prompt = build_prompt(alarm)

    # --- Bedrock call (commented; wire when creds/policy exist) ---
    # br = boto3.client("bedrock-runtime", region_name=os.getenv("BEDROCK_REGION"), config=Config(retries={'max_attempts': 3}))
    # resp = br.invoke_model(
    #     modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    #     body=json.dumps({"prompt": prompt, "max_tokens": 400})
    # )
    # summary = json.loads(resp["body"].read()).get("completion")

    # For demo, emulate a response:
    summary = "Incident summary (demo): API latency elevated in us-east-1. Likely cause: DB connections saturation. Next: scale read replicas, enable connection pooling, check slow queries."

    out = {
        "when": datetime.datetime.utcnow().isoformat() + "Z",
        "summary": summary,
        "alarm_name": (alarm.get("alarmName") if isinstance(alarm, dict) else "unknown"),
    }

    # --- S3 write (commented) ---
    # s3 = boto3.client("s3")
    # s3.put_object(Bucket=os.environ["SUMMARY_BUCKET"], Key=f"incidents/{out['when']}.json", Body=json.dumps(out).encode())

    # --- Slack webhook (optional, commented) ---
    # if os.getenv("SLACK_WEBHOOK"):
    #     import urllib.request
    #     urllib.request.urlopen(urllib.request.Request(os.getenv("SLACK_WEBHOOK"), data=json.dumps({"text": out["summary"]}).encode(), headers={"Content-Type":"application/json"}))

    return {"statusCode": 200, "body": json.dumps(out)}
