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
skills/hackathon-scoper/SKILL.md   the skill itself (drop into ~/.claude/skills/)
examples/example-output.md         a full run on a sample team (SnapSolve)
TRANSCRIPT.md                       transcript of building + running the skill
```

## Try it

Copy the skill into your Claude Code skills directory:

```bash
cp -r skills/hackathon-scoper ~/.claude/skills/
```

Then in Claude Code:

```
/hackathon-scoper

Idea: <2-3 sentences>
Tech stack: <languages, frameworks, APIs>
Team: <e.g. 3 people — 2 fullstack devs, 1 designer>
```

It will ask for any of the three inputs you leave out, then produce the plan.

## Why I built it

I'm Arjun Pun Magar, a CS junior at the University of Southern Mississippi and a
Break Through Tech AI Fellow at Cornell Tech. I build AI-native projects
end-to-end. This skill is my answer to MLH's "build an agent skill useful at a
hackathon" prompt — the scoping conversation is the highest-leverage 10 minutes
of any 24-hour build, so I turned it into a repeatable tool.
