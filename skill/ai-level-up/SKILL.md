---
name: ai-level-up
description: AI Level Up, an evidence-based RPG that tracks and gamifies a person's growth from AI user to AI systems operator, with XP, levels, seven skill trees, quests, boss battles and badges, saved to a player-record file. Use when the user says "Start" for AI Level Up, "Status Report", "Quest Board", "Mission Complete:", "Level Up", "Boss Battle", "Save Game", "Load Game" "Recalibrate" or "Dashboard", or asks to level up, track, score or gamify their AI skills.
---

# AI Level Up (file-backed)

The game rules live in [references/rules.md](references/rules.md). Read that file in full the first time this skill runs in a session. It is the game. Everything below only covers how to keep the save file.

## Player record

- The record is `AI_LEVEL_UP.md` in the working directory, unless the user names another path.
- **No record yet:** run onboarding from the rules, then create the record from [templates/player-record.md](templates/player-record.md).
- **Record exists:** read it before every command, and treat it as the source of truth over anything remembered from earlier chats.
- After any change to XP, score, quests or badges, update the record and set the last-evaluation date to today.
- Before paying XP, check the completed-quest log for an earlier award for the same completion.
- When a claim can be checked against files the session can read (a finished video, a script, a log), check it and tag the award V. Otherwise tag it R.
- The file is the save, so don't print a SAVE STATE block after every change. Print one only on `Save Game`, so the player can carry progress to a chat model without file access.
- `Load Game: [state]` merges a pasted SAVE STATE into the record. Show what changes and confirm before overwriting.
- Say progress was saved only after the write succeeded.

## Dashboard

On `Dashboard`, after onboarding, and on `Level Up`, build the visual command center from [assets/dashboard.html](assets/dashboard.html). Use this template instead of designing a new page, so every player gets the same interface.

1. Convert the record to the save-code JSON described in the rules (`SAVE STATE`).
2. Copy the template and put that JSON between `<script id="ailu-state" type="application/json">` and `</script>`. Escape any `</` in the JSON as `<\/`.
3. Where the session can write files, save it as `ai-level-up-dashboard.html` next to the record and open it. Where Artifacts are available, publish it as an artifact instead.

The text HUD from the rules still opens every Status Report.
