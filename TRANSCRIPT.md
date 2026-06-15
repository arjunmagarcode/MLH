# Build + run transcript — Hackathon Scoper

This is the record Swift asked for: the skill being built and run end-to-end.

## 1. The ask

MLH's application prompt: *"Write an agent skill that would be useful at a
hackathon."* Swift's follow-up: *"Actually build the skill you're describing and
send me the output + transcript."*

## 2. What the skill is

A Claude Code agent skill — a `SKILL.md` with YAML frontmatter (name +
description that tells Claude when to invoke it) and a body of instructions that
define the agent's behavior. The full skill lives at
[`skills/hackathon-scoper/SKILL.md`](skills/hackathon-scoper/SKILL.md).

Its contract:
- **Inputs:** idea, tech stack, team. It refuses to invent an idea and asks for
  any missing input rather than guessing.
- **Behavior:** acts as a scoping mentor whose bias is to *cut* scope to what
  demos well.
- **Output:** eight fixed sections — name/one-liner, reality check, MVP
  checklist (MUST/SHOULD/NICE + hours), 24h timeline with owners, APIs worth
  integrating, 3 stretch goals, biggest risk, demo tip.

## 3. Running it

**Input pasted by a sample team:**

```
Idea: A web app where you photograph a handwritten math problem and get a
step-by-step solution plus a short voice explanation. Targeting education.
Tech stack: Next.js, Tailwind, Python/FastAPI, Claude API (vision + text),
ElevenLabs TTS, Supabase.
Team: 3 people — 2 fullstack devs, 1 designer.
Scope this for a 24-hour hackathon. Be brutally practical.
```

**Output produced:** the full scoped plan for "SnapSolve" — see
[`examples/example-output.md`](examples/example-output.md) for the complete run.

Highlights that show the skill is doing real scoping work, not generic advice:
- It demoted live camera capture from a MUST to a SHOULD and named input-UX
  scope creep as the single biggest risk — the actual failure mode for this idea.
- It set a hard feature freeze at hour 20 and reserved 22–24h purely for demo
  rehearsal + a recorded backup.
- Every API got a complexity rating, and it flagged KaTeX (not the AI) as the
  medium-complexity time sink.
- MUST tasks total ~13h across 3 people — deliberately inside the window with
  slack for the 2am wall.

## 4. Edge case handled

When run with the template placeholders left unfilled (`Idea: [describe...]`),
the skill does **not** fabricate a project. It detects the missing inputs and
asks for the real idea, stack, and team first. Scoping a hallucinated idea is
worse than asking one question.

## 5. Result

A working, reusable skill any team can drop into Claude Code and run at hour 0.
Repo: this directory.
