# AI Level Up

**Level up how you use AI, and prove it.**

AI Level Up turns any AI chatbot into a game master that tracks your growth from casual AI user to AI systems operator. You earn XP for things you actually finish and ship, level up through six tiers, build seven skill trees, take on quests built around your own projects, and fight boss battles aimed at your weakest skills.

It is built to be hard to cheat. Plans earn nothing, vague claims earn nothing, and your skill score only moves when you show evidence.

Works with ChatGPT, Claude, Gemini, Grok, Copilot, Llama, Mistral, or any model that accepts instructions.

---

## What's in this folder

| File | Use it for |
|---|---|
| `AI_LEVEL_UP_PROMPT.md` | **The game.** One prompt for any model. Under 8,000 characters, so it fits a Custom GPT. |
| `skill/ai-level-up/` | A Claude skill version that saves your progress to a file automatically. |
| `ai-level-up-skill.zip` | The same skill, zipped for upload. |

---

## Setup (2 minutes)

1. Open [`AI_LEVEL_UP_PROMPT.md`](AI_LEVEL_UP_PROMPT.md) and click the **Copy raw file** button at the top right.
2. Paste it into your model (steps below).
3. Type **`Start`**.

### ChatGPT
- **Best:** Explore GPTs → Create → Configure → paste the prompt into **Instructions**. Name it "AI Level Up".
- **Or:** Create a Project and paste the prompt into the project's instructions.
- **Quick try:** paste the prompt as your first message in a new chat.

### Claude (claude.ai)
- **Best:** upload `ai-level-up-skill.zip` as a skill in Settings (under Capabilities → Skills, if your plan has skills).
- **Or:** create a Project and paste the prompt into the project instructions.
- **Quick try:** paste the prompt as your first message.

### Claude Code / Claude desktop
Copy the skill folder into your skills directory:
```bash
cp -R skill/ai-level-up ~/.claude/skills/
```
Your progress is saved to `AI_LEVEL_UP.md` in whatever folder you're working in.

### Gemini
Gems → New Gem → paste the prompt into **Instructions**.

### Grok, Copilot, Perplexity, local models, anything else
Paste the prompt as the system prompt or custom instructions. If the model has no instructions field, paste it as your first message.

---

## Commands

| Type | What happens |
|---|---|
| `Start` | A 2-round calibration interview, then your starting dashboard |
| `Status Report` | Level, XP bar, score, skill scorecard, top quests, biggest obstacle, one next action |
| `Quest Board` | Your active quests, ranked, with XP and completion criteria |
| `Mission Complete: …` | Submit something you finished. Include a link or specifics. |
| `Level Up` | What you unlocked and your next real challenge |
| `Boss Battle` | One ambitious project aimed at your weakest skills |
| `Save Game` | Prints your save code |
| `Load Game: …` | Paste a save code to pick up where you left off |
| `Recalibrate` | Re-score your skills from evidence (once a month) |

---

## Saving your progress

Most chatbots forget between chats. The game handles this with a **save code**: a short `AI_LEVEL_UP_STATE` block it prints whenever your XP, score, quests or badges change.

1. Copy the latest save code into a note (or a file in your ChatGPT/Claude Project).
2. In a new chat, type `Load Game:` and paste it.

The save code is plain text, so you can switch models mid-campaign. Start on ChatGPT, then continue on Claude or Gemini.

The Claude skill version saves to a file instead, so you don't need save codes there.

---

## How scoring works

- **XP and levels** reward finishing things: 50 XP for a finished piece of work, 100 XP for putting it in front of real people, 150–250 XP for workflows and systems you build and actually run. `Level = 1 + floor(XP / 200)`.
- **Tiers:** Initiate (1–4) → Builder (5–9) → Operator (10–14) → Systems Architect (15–19) → Commander (20–29) → Vanguard (30+).
- **Your skill score (0–10)** is separate from XP. It only moves with evidence, never because you leveled up.
- **Past work counts, but only so much.** At onboarding, accomplishments you describe specifically earn Legacy XP, capped at 800 (Level 5). Everyone still has to earn their way up.
- **Evidence is tagged.** V (verified: a link, file, screenshot or metric) or R (reported: a specific claim). A skill above 8.0 needs at least one verified item.

## The seven skill trees

1. Curiosity & Exploration
2. Context Engineering & Prompting
3. Multi-Model Orchestration
4. Practical Application
5. Teaching & Community
6. Building AI Systems
7. Execution & Shipping

---

## Running it with a group

Workshop facilitators can use this as a cohort game:
- Everyone runs `Start` at the first session and shares their starting level.
- Each week, people post their `Status Report` progress bar.
- Boss Battles make good capstone projects.

---

## Customizing

The prompt is plain text. Edit the XP table, rename the tiers, or add badges for your team or community. If you share a modified version, keep the Prime Directives. They're what stop the game from rewarding plans over results.

---

*Built by Chicago AI Forge · chicagoaiforge.com*
