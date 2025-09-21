# AWS Incident Summarizer (CloudWatch → Lambda → Bedrock)

Goal: When a CloudWatch alarm fires, generate a short, actionable incident summary using a Bedrock model.
Outputs can go to S3 and (optionally) Slack.

Flow:
CloudWatch Alarm → EventBridge → Lambda (parse alarm JSON) → Bedrock prompt → store in S3

Enable later:
- IAM role for Lambda with bedrock:InvokeModel and s3:PutObject.
- Slack webhook (optional).

Environment:
- BEDROCK_REGION, SUMMARY_BUCKET, (optional) SLACK_WEBHOOK
