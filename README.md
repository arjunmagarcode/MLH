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

## Demo

A live run (model: `llama-3.3-70b-versatile`) scoping a handwritten-math-solver idea.

**Input:**

```
Idea: A web app where you photograph a handwritten math problem and get a
step-by-step solution with a short voice explanation. Targets the education track.
Tech stack: Next.js, Tailwind, Python/FastAPI, Groq API, ElevenLabs TTS, Supabase
Team: 3 people — 2 fullstack devs, 1 designer
```

**Output:**

```
PROJECT NAME & ONE-LINER
MathSolve: A web app that uses AI to solve handwritten math problems and
provides step-by-step audio explanations.

REALITY CHECK
Given the complexity of the project, which involves image processing, math
problem solving, and text-to-speech integration, it's highly unlikely that we
can deliver a fully polished product within 24 hours. However, we can aim to
build a functional prototype that demonstrates the core functionality. The
biggest challenge will be integrating the various APIs and handling the image
processing and math problem solving.

MVP CHECKLIST
* MUST (4h): Set up Next.js project with basic UI using Tailwind (1h), integrate
  Supabase for storing user data (1h), create a simple API using FastAPI for
  handling image uploads (1h), and basic math problem solving (1h)
* MUST (4h): Integrate Groq API for math problem solving (2h) and ElevenLabs TTS
  for audio explanations (2h)
* SHOULD (4h): Implement image processing using a library like OpenCV (2h) and
  integrate it with the FastAPI backend (2h)
* NICE (4h): Implement a more advanced UI with features like problem editing and
  history (2h), and add more advanced math problem solving capabilities (2h)

24-HOUR TIMELINE
* 0-2h: Project setup, team discussion, and task assignment
* 2-6h: Set up Next.js project, integrate Supabase, and create basic API using
  FastAPI (Owner: Fullstack Dev 1)
* 6-10h: Integrate Groq API and ElevenLabs TTS (Owner: Fullstack Dev 2)
* 10-14h: Implement image processing and integrate it with the FastAPI backend
  (Owner: Fullstack Dev 1)
* 14-18h: Feature freeze, focus on integration and debugging
* 18-20h: Demo preparation, UI polishing, and audio testing (Owner: Designer)
* 20-24h: Final debugging, demo rehearsal, and submission preparation

APIS WORTH INTEGRATING
* Groq API (medium): Provides advanced math problem solving capabilities
* ElevenLabs TTS (low): Offers high-quality text-to-speech functionality
* Supabase (low): Provides a simple and easy-to-use database solution
* OpenCV (medium): Offers advanced image processing capabilities
* Google Cloud Vision API (high): Provides advanced image recognition and
  processing capabilities (optional)

STRETCH GOALS
* Implement a feature to edit and save math problems
* Add support for more advanced math topics like calculus and algebra
* Integrate a feature to share and discuss math problems with others

BIGGEST RISK
The biggest risk is the integration of the various APIs, especially the Groq API
and ElevenLabs TTS, which may require significant debugging and tweaking to work
seamlessly. Mitigation: Allocate sufficient time for integration and debugging,
and have a backup plan in case one of the APIs doesn't work as expected.

DEMO TIP
Focus on demonstrating the core functionality of the app, which is solving
handwritten math problems and providing step-by-step audio explanations. Make
sure to test the demo thoroughly to ensure that it works smoothly and without
any technical issues.
```

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
