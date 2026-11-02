# AI LEVEL UP — Player Record

> Persistent state for the AI Level Up campaign. Read before every update; save after.

| Field | Value |
|---|---|
| Player | |
| Started | YYYY-MM-DD |
| Last evaluation | YYYY-MM-DD |
| Mirror Test | — / 5 |
| Power User Score | X.X / 10 (prev —) |
| Prestige | 0 |
| Lifetime XP | 0 |
| Season XP (since last Prestige) | 0 |
| Level | 1 — Initiate |
| Next level | Level 2 (0 / 200 XP) |

Level formula: `Level = 1 + floor(season XP / (200 + 100 × prestige))`

---

## 1. Score history

| Date | Score | Change | Evidence |
|---|---:|---:|---|

## 2. Skill scorecard

| # | Tree | Score | Read |
|---|---|---:|---|
| 1 | Curiosity & Exploration | | |
| 2 | Context & Personalization | | |
| 3 | Connecting Tools | | |
| 4 | Judgment | | |
| 5 | Practical Application | | |
| 6 | Teaching & Community | | |
| 7 | Building AI Systems | | |
| 8 | Execution & Shipping | | |

## 3. Skill trees

For each tree: **Demonstrated**, **Gap**, **Next unlock**, **Challenge**.

## 4. Quest board

### Main Quests
| ID | Quest | Completion criteria | Progress | Reward | Status |
|---|---|---|---|---|---|

### Weekly Quests
| ID | Quest | Completion criteria | Reward | Status |
|---|---|---|---|---|

### Daily Quests
| ID | Quest | Completion criteria | Reward | Status |
|---|---|---|---|---|

### Boss Battles
| ID | Boss | Requires | Reward |
|---|---|---|---|

## 5. Completed quest log

| Date | ID | Event | XP | V/R |
|---|---|---|---:|---|

## 6. Achievements

### Milestone counts
| Track | Count | Rank |
|---|---:|---|
| Transmitter (items published) | 0 | — |
| Questrunner (quests done) | 0 | — |
| Streak (weeks in a row) | 0 | — |
| Mentor (people taught) | 0 | — |
| Force Multiplier (hours saved / week) | 0 | — |
| Full Throttle (feature areas in use) | 0 | — |

### Rank insignia
Initiate ◆ · Builder ◇ · Operator ◇ · Systems Architect ◇ · Commander ◇ · Vanguard ◇

### Earned
| Badge | Date | Evidence |
|---|---|---|

### Locked
| Badge | Unlock condition |
|---|---|

## Armory

Written by the dashboard. Copy it unchanged into the save code.

```json
{}
```

## 7. Evidence log for score changes

| Date | Change | Evidence |
|---|---|---|
