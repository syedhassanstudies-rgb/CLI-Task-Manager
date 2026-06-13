import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def suggest_task_details(title: str, description: str) -> dict:
    prompt = f"""You are a productivity assistant. Analyze this task and suggest a priority and estimated time.

Task Title: {title}
Task Description: {description}

Respond in this exact format and nothing else:
Priority: <low/medium/high>
Estimated Time: <e.g. 30 minutes, 2 hours, 1 day>
Reason: <one sentence explaining why>"""

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.3,
    )

    raw = response.choices[0].message.content.strip()

    result = {
        "priority": "medium",
        "estimated_time": "unknown",
        "reason": ""
    }

    for line in raw.split("\n"):
        if line.startswith("Priority:"):
            result["priority"] = line.replace("Priority:", "").strip().lower()
        elif line.startswith("Estimated Time:"):
            result["estimated_time"] = line.replace("Estimated Time:", "").strip()
        elif line.startswith("Reason:"):
            result["reason"] = line.replace("Reason:", "").strip()

    return result