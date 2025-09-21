from fastapi import FastAPI, Request
import os, json

app = FastAPI()

SYSTEM = "You are a release notes assistant. Summarize features for end-users and list technical changes for engineers."

def build_prompt(commits):
    # Keep it pragmatic and structured
    return f"""Summarize these commits for two audiences.

1) End-user release notes (bullets, friendly tone).
2) Technical changelog (concise, with modules/services touched).

Commits JSON (truncated):
{json.dumps(commits)[:4000]}
"""

@app.post("/summarize")
async def summarize(req: Request):
    data = await req.json()
    prompt = build_prompt(data.get("commits", []))

    # ---- Vertex AI call (commented) ----
    # from vertexai.generative_models import GenerativeModel
    # import vertexai
    # vertexai.init(project=os.getenv("GOOGLE_CLOUD_PROJECT"), location=os.getenv("LOCATION", "us-central1"))
    # model = GenerativeModel(os.getenv("MODEL", "gemini-1.5-pro"))
    # resp = model.generate_content([SYSTEM, prompt])
    # summary = resp.text

    # Demo response
    summary = {
        "release_notes": ["New billing dashboard with CSV export.", "Faster login flow; less friction for MFA."],
        "tech_changelog": ["refactor(auth): reduce token roundtrips", "feat(billing): add /reports endpoint"],
    }
    return summary
