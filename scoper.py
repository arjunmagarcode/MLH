#!/usr/bin/env python3
"""Hackathon Scoper — turn a team's idea + stack into a scoped 24h build plan.

Runs the `hackathon-scoper` agent skill against a free, OpenAI-compatible LLM
API (Groq by default). Zero dependencies — Python standard library only.

Usage:
    export GROQ_API_KEY=gsk_...            # free key from console.groq.com
    python3 scoper.py                      # interactive: prompts for inputs
    python3 scoper.py --file team.txt      # read the brief from a file
    echo "Idea: ... Tech stack: ... Team: ..." | python3 scoper.py   # stdin

Config via env vars:
    GROQ_API_KEY   required (or OPENAI_API_KEY if you point at another endpoint)
    SCOPER_MODEL   default: llama-3.3-70b-versatile
    SCOPER_BASE    default: https://api.groq.com/openai/v1
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SKILL_PATH = Path(__file__).parent / "skills" / "hackathon-scoper" / "SKILL.md"
BASE = os.environ.get("SCOPER_BASE", "https://api.groq.com/openai/v1")
MODEL = os.environ.get("SCOPER_MODEL", "llama-3.3-70b-versatile")
API_KEY = os.environ.get("GROQ_API_KEY") or os.environ.get("OPENAI_API_KEY")


def load_system_prompt() -> str:
    """Use the skill's instructions (everything after the YAML frontmatter) as
    the system prompt, so the code and the skill never drift apart."""
    text = SKILL_PATH.read_text(encoding="utf-8")
    if text.startswith("---"):
        # drop the frontmatter block between the first two '---' fences
        _, _, body = text.split("---", 2)
        return body.strip()
    return text.strip()


def read_brief() -> str:
    """Get the team's brief from --file, stdin, or an interactive prompt."""
    if "--file" in sys.argv:
        path = sys.argv[sys.argv.index("--file") + 1]
        return Path(path).read_text(encoding="utf-8").strip()
    if not sys.stdin.isatty():
        piped = sys.stdin.read().strip()
        if piped:
            return piped
    print("Describe your hackathon project. Fill in all three lines:\n")
    idea = input("Idea (2-3 sentences): ").strip()
    stack = input("Tech stack: ").strip()
    team = input("Team (e.g. 3 people — 2 fullstack, 1 designer): ").strip()
    return f"Idea: {idea}\nTech stack: {stack}\nTeam: {team}\n\nScope this for a 24-hour hackathon. Be brutally practical."


def call_llm(system: str, user: str) -> str:
    """POST to an OpenAI-compatible chat-completions endpoint."""
    payload = json.dumps({
        "model": MODEL,
        "temperature": 0.4,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE}/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def main() -> int:
    if not API_KEY:
        sys.exit("Error: set GROQ_API_KEY (free key at https://console.groq.com).")
    system = load_system_prompt()
    brief = read_brief()
    if not brief:
        sys.exit("Error: no project brief provided.")
    print("\nScoping your build... (model: %s)\n" % MODEL, file=sys.stderr)
    try:
        print(call_llm(system, brief))
    except urllib.error.HTTPError as e:
        sys.exit(f"API error {e.code}: {e.read().decode('utf-8', 'replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"Network error: {e.reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
