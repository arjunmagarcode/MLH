# Example run — `hackathon-scoper`

This is the skill run end-to-end on a realistic team. The input below is exactly
what a team would paste at hour 0; the output is what the skill produced.

---

## INPUT

> **Idea:** A web app where you photograph a handwritten math problem and get a
> step-by-step solution plus a short voice explanation. Targeting the education
> track.
>
> **Tech stack:** Next.js, Tailwind, Python/FastAPI, Claude API (vision + text),
> ElevenLabs TTS, Supabase.
>
> **Team:** 3 people — 2 fullstack devs, 1 designer.
>
> Scope this for a 24-hour hackathon. Be brutally practical.

---

## OUTPUT

### PROJECT NAME & ONE-LINER
**SnapSolve** — Photograph any handwritten math problem and get a worked,
step-by-step solution that talks you through it.

### REALITY CHECK
Very doable, and the pieces are all hosted APIs you're gluing together rather
than models you're training — that's the right shape for 24 hours. The real
danger isn't the AI; it's that you'll burn the night polishing the camera/upload
UX and the voice playback instead of locking the one flow that wins the demo. If
the photo→solution path is rock-solid by hour 14, everything after that is gravy.

### MVP CHECKLIST
- **MUST** — Image upload (file picker, not live camera) → FastAPI endpoint · *2h*
- **MUST** — Claude vision call: image → transcribed problem + step-by-step solution (structured JSON) · *3h*
- **MUST** — Render steps cleanly in the UI (KaTeX for math, numbered steps) · *3h*
- **MUST** — ElevenLabs TTS on the explanation text + a play button · *2h*
- **MUST** — One polished end-to-end happy path, deployed to a public URL · *3h*
- **SHOULD** — Live camera capture on mobile (getUserMedia) · *2h*
- **SHOULD** — Supabase: save solved problems to a history list · *2h*
- **SHOULD** — Loading/error states so a bad photo doesn't crash the demo · *1.5h*
- **NICE** — "Explain this step differently" re-prompt button · *1.5h*
- **NICE** — Share/export solution as an image or link · *1.5h*

MUSTs total ~13h of focused work across 3 people — comfortably inside the window.

### 24-HOUR TIMELINE
- **0–2h — Setup & contract (all 3):** Repo, deploy targets (Vercel + a FastAPI host), API keys in env, and *agree on the JSON shape* Claude returns. This contract lets frontend and backend work in parallel.
- **2–6h — Parallel core build:** Dev A → FastAPI + Claude vision endpoint returning the agreed JSON. Dev B → upload UI + steps renderer against a mocked JSON response. Designer → layout, typography, the "result card" that the demo lives on.
- **6–14h — Integration + voice:** Wire real backend to real frontend (this is where time disappears — protect it). Add ElevenLabs TTS. Get one full photo→solution→voice flow working on the deployed URL, not just localhost.
- **14–20h — SHOULDs + hardening:** Camera capture, Supabase history, error states. Stop adding features the moment the happy path feels fragile.
- **20–22h — FEATURE FREEZE:** No new features. Only bug fixes, copy, and visual polish. Pick the exact problem photo you'll demo and make it flawless.
- **22–24h — Demo prep (all 3):** Rehearse the 2-minute run twice. Pre-load the demo problem. Record a 30s backup video in case wifi or an API dies on stage.

### APIS WORTH INTEGRATING
- **Claude API (vision + text)** — Does the heavy lifting: reads handwriting and produces structured steps in one call. *Complexity: low.*
- **ElevenLabs TTS** — The voice explanation is your "wow" differentiator vs. every other text-only solver. *Complexity: low.*
- **Supabase** — Free auth + Postgres for problem history with almost no backend code. *Complexity: low.*
- **KaTeX (client lib, not an API)** — Renders the math so output looks professional, not like plaintext. *Complexity: medium* (LaTeX edge cases eat time).
- **Vercel / Render** — One-command deploys so judges hit a real URL. *Complexity: low.*

### STRETCH GOALS
1. "Explain it like I'm 10" toggle that re-prompts Claude for a simpler explanation.
2. Step-by-step reveal — show one step at a time with the voice narrating each.
3. Multi-problem worksheet: photograph a whole page, solve every problem on it.

### BIGGEST RISK
**Scope creep around input UX** — live camera, cropping, and multi-photo handling
will quietly eat your whole night. *Mitigation:* ship file-upload first and treat
the camera as a SHOULD, not a MUST.

### DEMO TIP
Open with the photo and the *voice already explaining* within 10 seconds — lead
with the magic moment, not a login screen. Use a pre-tested problem photo and a
recorded backup so a flaky network can't kill your run on stage.
