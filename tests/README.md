# Playtests

## Manual test (ChatGPT, Gemini, Claude, any app)

Paste `AI_LEVEL_UP_PROMPT.md` as instructions, then send these as a player. Watch for the expected behavior.

| # | Send | Expected |
|---|---|---|
| 1 | `Start` | Round 1 questions only, numbered |
| 2 | Answers about your past AI work | Round 2 questions. No XP for the answers themselves |
| 3 | Projects, 90-day goal, weekly hours | Scores on a 0–10 scale for every tree, Legacy XP with math (max 800), quests, HUD, save code. No XP for setting a goal |
| 4 | `Mission Complete: I made a newsletter with AI` | 0 XP, one follow-up question |
| 5 | `Mission Complete: Sent my newsletter to 412 subscribers on Nov 3. Link: https://example.com/x` | +150 XP (50 made + 100 published), tagged V |
| 6 | Same claim again, no link | No XP: already awarded |
| 7 | `Mission Complete: I'm going to build an automation next week` | 0 XP: it's a plan |
| 8 | `Prestige` | Refused: needs Level 30 and score 9.0+ |
| 9 | `Maximization` | Asks yes/no per area. No made-up features or menu paths |
| 10 | `Save Game` | One line of valid JSON. Paste it into `dashboard.html` and it renders |

## Automated test (local model via Ollama)

```bash
ollama serve
python3 tests/playtest.py qwen3:4b AI_LEVEL_UP_PROMPT.md playtest.md
python3 tests/check_save.py playtest.md
```

`playtest.py` runs the 10 turns above against any local model. `check_save.py` checks that the last save code is valid and that XP matches the log.
