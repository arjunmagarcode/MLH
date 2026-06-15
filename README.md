# Hackathon Scoper — an agent skill for hour 0

> The conversation every hackathon team needs at hour 0 but rarely has well.

**Hackathon Scoper** is a [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
agent skill. You give it a team's idea, tech stack, and headcount; it returns a
brutally practical, scoped **24-hour build plan**:

- a **reality check** on whether the idea fits in 24 hours,
- an **MVP checklist** tagged MUST / SHOULD / NICE with hour estimates,
- an **hour-by-hour timeline** with owners and a built-in feature freeze,
- **APIs worth integrating** with complexity ratings,
- **stretch goals**, the **biggest risk**, and a **demo tip**.

Teams lose hackathons by building too much, not too little. This skill exists to
cut scope to the thing that actually demos — at the one moment cutting is cheap.

## What's here

```
scoper.py                          runnable CLI — calls a free LLM API
skills/hackathon-scoper/SKILL.md   the skill / system prompt the CLI runs on
```

## Run the code (free, zero dependencies)

`scoper.py` is pure Python standard library — no `pip install`. It uses
[Groq's free API](https://console.groq.com) by default, and reads its system
prompt straight from `SKILL.md`, so the code and the skill never drift apart.

```bash
export GROQ_API_KEY=gsk_...        # free key from console.groq.com
python3 scoper.py                  # answer the three prompts interactively
python3 scoper.py --file brief.txt # or read the brief from a file
echo "Idea: ...  Tech stack: ...  Team: ..." | python3 scoper.py   # or pipe it in
```

It's endpoint-agnostic — point it at any OpenAI-compatible API by setting
`SCOPER_BASE` and `SCOPER_MODEL` (e.g. a local Ollama server, Gemini's
OpenAI-compatible endpoint, etc.).

## Or run it as a Claude Code skill

Copy the skill into your Claude Code skills directory:

```bash
cp -r skills/hackathon-scoper ~/.claude/skills/
```

Then in Claude Code: `/hackathon-scoper`, paste your idea / stack / team, and it
produces the plan. It asks for any of the three inputs you leave out.

## Why I built it

I'm Arjun Pun Magar, a CS junior at the University of Southern Mississippi and a
Break Through Tech AI Fellow at Cornell Tech. I build AI-native projects
end-to-end. This skill is my answer to MLH's "build an agent skill useful at a
hackathon" prompt — the scoping conversation is the highest-leverage 10 minutes
of any 24-hour build, so I turned it into a repeatable tool.
