# AI Level Up

**Level up how you use AI, and prove it.**

AI Level Up turns any AI chatbot into a game master that tracks your growth from casual AI user to AI systems operator. You earn XP for things you actually finish and ship, level up through six tiers, build eight skill trees, take on quests built around your own projects, fight boss battles aimed at your weakest skills, earn milestone badges, and keep climbing with Prestige once you max out. Your XP also earns credits you spend in the Armory on gear for your cyberpunk avatar.

It is built to be hard to cheat. Plans earn nothing, vague claims earn nothing, and your skill score only moves when you show evidence.

Works with ChatGPT, Claude, Gemini, Grok, Copilot, Llama, Mistral, or any model that accepts instructions.

---

## What's in this folder

| File | Use it for |
|---|---|
| `AI_LEVEL_UP_PROMPT.md` | **The game.** One prompt for any model. Under 8,000 characters, so it fits a Custom GPT. |
| `MAXIMIZATION.md` | Optional field guide for the Maximization scan: the 10 feature areas and where they live in each AI app. Add it as a knowledge file for a sharper audit. |
| `dashboard.html` | Your command center and Armory. Open it in any browser, paste your save code, see everything at a glance and gear up your avatar. Works offline. |
| `dashboard/` | The dashboard's source and its D3 charting library. Edit here, then run `python3 build.py`. |
| `build.py` | Builds `dashboard.html` and the skill zip. |
| `skill/ai-level-up/` | A Claude skill version that saves your progress to a file automatically. |
| `ai-level-up-skill.zip` | The same skill, zipped for upload. |
| `tests/` | A 10-turn playtest script to check the game in any model, plus an automated version for local models. |

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
| `Mirror Test` | Checks how well your AI knows you: 5 questions, scored out of 5 |
| `Maximization` | Scans which features of your AI app you use and gives you the 3 unused ones that would help most |
| `Dashboard` | Your visual command center (see below) |
| `Save Game` | Prints your save code |
| `Load Game: …` | Paste a save code to pick up where you left off |
| `Use Perk: …` | Spend a perk you bought in the Armory, such as `Use Perk: Quest Reroll` |
| `Recalibrate` | Re-score your skills from evidence (once a month) |
| `Prestige` | Reset your level for a Prestige star once you hit Level 30 with a 9.0+ score (optional) |

---

## Saving your progress

Most chatbots forget between chats. The game handles this with a **save code**: a one-line block of JSON it prints whenever your XP, score, quests or badges change.

1. Copy the latest save code into a note (or a file in your ChatGPT/Claude Project).
2. In a new chat, type `Load Game:` and paste it.

The save code is plain text, so you can switch models mid-campaign. Start on ChatGPT, then continue on Claude or Gemini.

The Claude skill version saves to a file instead, so you don't need save codes there.

---

## Your command center

Every Status Report opens with a text HUD that works in any chat:

```
╔═ AI LEVEL UP // COMMAND CENTER ═══════════════╗
 CALLSIGN  Nova             LVL 6 · BUILDER
 XP        1,130  ██████░░░░  130/200 → LVL 7
 SCORE     6.8 / 10  ▲ 0.4
 PLATFORM  ChatGPT Plus     █████░░░░░ 5/10
 MIRROR    3/5
 ─ SKILL TREES ─────────────────────────────────
 Curiosity      ████████░░ 8.2
 Connecting Tools █████░░░ 5.1
 ...
╚═══════════════════════════════════════════════╝
```

For the full visual version, open [`dashboard.html`](dashboard.html) in a browser, paste your save code, and click **Open command center**. Click **Try a demo** to see a new player, or **Elite demo** to see a Prestige 2 player. It's one file with no outside requests, so it works offline and your save code never leaves your browser. The Claude skill fills it in with your record and opens it for you.

It has three tabs:

- **Command:** your avatar, level ring, XP and credits, a D3 skill-matrix radar of all eight trees, score history, quests, Maximization coverage, mission log, milestone tracks, insignia and badges.
- **Operative:** your avatar, your class (from your strongest skill tree), your loadout, and free appearance options: skin, hair, hair color and neon accent.
- **Armory:** try on and buy gear, and buy perks (see below).

---

## How scoring works

- **XP and levels** reward finishing things: 50 XP for a finished piece of work, 100 XP for putting it in front of real people, 150–250 XP for workflows and systems you build and actually run. `Level = 1 + floor(XP / 200)` until your first Prestige.
- **Tiers:** Initiate (1–4) → Builder (5–9) → Operator (10–14) → Systems Architect (15–19) → Commander (20–29) → Vanguard (30+).
- **Your skill score (0–10)** is separate from XP. It only moves with evidence, never because you leveled up.
- **Past work counts, but only so much.** At onboarding, accomplishments you describe specifically earn Legacy XP, capped at 800 (Level 5). Everyone still has to earn their way up.
- **Evidence is tagged.** V (verified: a link, file, screenshot or metric) or R (reported: a specific claim). A skill above 8.0 needs at least one verified item.

## The eight skill trees

1. Curiosity & Exploration
2. Context & Personalization: the context you give for each task, plus lasting context about who you are
3. Connecting Tools: getting AI to work with your apps, files and other AI tools
4. Judgment: checking AI output, catching errors, knowing when not to use AI, protecting private data
5. Practical Application
6. Teaching & Community
7. Building AI Systems
8. Execution & Shipping

Not every tree fits everyone on day one. During onboarding, a tree that doesn't apply to you yet is marked **Dormant**. It doesn't count against your score, and it wakes up the first time you show evidence for it.

---

## Badges

**Milestone tracks** rank up from Bronze to Silver, Gold and Platinum as your counts grow:

| Track | Counts | Bronze | Silver | Gold | Platinum |
|---|---|---:|---:|---:|---:|
| Transmitter | Items published | 1 | 10 | 50 | 100 |
| Questrunner | Quests completed | 10 | 50 | 150 | 500 |
| Streak | Weeks in a row with your weekly goal met | 4 | 12 | 26 | 52 |
| Mentor | People taught, with outcomes captured | 1 | 10 | 50 | 250 |
| Force Multiplier | Documented hours saved per week | 1 | 5 | 10 | 20 |
| Full Throttle | Feature areas in regular use | 4 | 6 | 8 | 10 |

**One-time badges** mark firsts: First Contact (first quest), Scout (kept or killed a tool, with a written verdict), Mirror Match (5/5 Mirror Test), Fact Checker (caught an AI error before it shipped), Workflow Engineer (first tested, reusable workflow), Connected (AI in a daily tool for a week), Systems Architect (a reliable connected system in use) and Boss Slayer (first Boss Battle won). The game master can also award custom badges for real milestones.

**Rank insignia** are earned for each tier you reach, from Initiate to Vanguard, and for each Prestige rank.

---

## Prestige

For people who reach the top. Prestige unlocks at **Level 30 (Vanguard) with a skill score of 9.0 or higher**. It's optional, and the game never pushes it.

When you type `Prestige`:
- You gain a Prestige star (★), with no limit on how many.
- Your level resets to 1. Your lifetime XP, badges and history stay.
- Each level costs 100 XP more than before: 300 XP per level at Prestige 1, 400 at Prestige 2, and so on.
- You get a **Mandate**: an elite Boss Battle you must win before you can Prestige again. Mandates are about multiplying your impact through other people and systems, such as three teams running your workflow every week without you.

Above a 9.5 skill score, only impact on others moves the number: people using your systems, people you trained, and hours saved. Playing well yourself isn't enough at that point.

---

## Armory

Every XP you earn also earns a **credit**. Spend credits in the dashboard's Armory. Your XP and level never go down when you buy something.

- **Gear is cosmetic:** 37 items across 7 slots (headgear, optics, armor, outerwear, cyberware, companion, backdrop), from 150-credit common items to 5,000-credit legendaries.
- **Some gear can't be bought.** It's earned: the Builder Harness at Level 5, the Signal Drone for your first published work, the Mirror Lens for a 5/5 Mirror Test, the Slayer Scar for your first Boss Battle win, the Vanguard Halo for Prestige.
- **Perks change how you play, never your XP or score:** Quest Reroll (100), Overclock for one extra Daily Quest (250), Streak Shield for one rest week (300), Early Recalibrate (500). Use one in your AI chat with `Use Perk: [name]`.
- **Your class** comes from your strongest skill tree: Scout, Whisperer, Netrunner, Sentinel, Fixer, Mentor, Technomancer or Courier. It changes as you grow.

Purchases are stored in the `armory` part of your save code. After you buy something, click **Copy save code** in the dashboard and send it to your AI with `Load Game:`, so your game master keeps your gear.

---

## Mirror Test

How well does your AI actually know you? Type **`Mirror Test`** in a fresh chat. The AI answers 5 questions about you using only what it has saved (memory, custom instructions, project files): your role, audience, goals, voice and style, and current projects. You mark each answer right or wrong.

Your score out of 5 is tracked over time. To raise it, complete the **About Me** quest: a one-page personal context document you can paste into any AI. Score 5/5 for the **Mirror Match** badge.

---

## Maximization

Most people use a fraction of what their AI app can do. Type **`Maximization`** and the game master audits your app and plan across 10 feature areas:

1. Customization & memory
2. Projects & workspaces
3. Skills, GPTs & Gems
4. Files & knowledge
5. Plug-ins & connectors
6. Deep research
7. Creation tools (canvas, artifacts, images, video)
8. Voice & vision
9. Automation & agents
10. Code & data

You get a coverage score (for example 5/10) and the 3 unused features that would pay off most for *your* projects. Each comes with a 5-minute setup step and a Daily Quest. Adopting a feature (using it on real work 3 times) earns +50 XP. Areas in regular use count toward the **Full Throttle** milestone track.

It works in any app. For a more detailed audit, add [`MAXIMIZATION.md`](MAXIMIZATION.md) as a knowledge file. It maps each area to feature names in ChatGPT, Claude, Gemini, Copilot, Grok, Perplexity and local models.

---

## Running it with a group

Workshop facilitators can use this as a cohort game:
- Everyone runs `Start` at the first session and shares their starting level.
- Each week, people post their `Status Report` progress bar.
- Boss Battles make good capstone projects.

---

## Customizing

The prompt is plain text. Edit the XP table, rename the tiers, or add badges for your team or community. To change the gear, perks or prices, edit the catalog in `dashboard/dashboard.src.html` and run `python3 build.py`. If you share a modified version, keep the Prime Directives. They're what stop the game from rewarding plans over results.

---

*Built by Chicago AI Forge · chicagoaiforge.com*
