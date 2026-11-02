"""Pull the last save code out of a playtest transcript and check it against the v2 schema."""
import json
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
cands = re.findall(r"\{\s*\"v\"\s*:.*?\}(?=\s*(?:```|~~~|$))", text, re.S)
if not cands:
    sys.exit("NO SAVE CODE FOUND")
raw = cands[-1]
try:
    s = json.loads(raw)
except Exception as e:
    sys.exit(f"INVALID JSON: {e}\n{raw[:400]}")

problems = []
need = ["v", "player", "score", "xp", "season_xp", "prestige", "trees", "platform", "mirror", "counts", "badges", "quests", "log", "armory"]
problems += [f"missing key: {k}" for k in need if k not in s]
trees = s.get("trees", {})
for k in ["curiosity", "context", "connecting", "judgment", "application", "teaching", "systems", "shipping"]:
    if k not in trees:
        problems.append(f"missing tree: {k}")
log_xp = sum(int(l.get("xp", 0) or 0) for l in s.get("log", []))
if log_xp and log_xp != s.get("xp"):
    problems.append(f"xp {s.get('xp')} != sum of log {log_xp}")
ids = [l.get("id") for l in s.get("log", [])]
if len(ids) != len(set(ids)):
    problems.append(f"duplicate log ids: {ids}")
if s.get("xp", 0) > 0 and s.get("prestige", 0) == 0 and s.get("season_xp") not in (None, s.get("xp")):
    problems.append("season_xp should equal xp before any Prestige")
xp = s.get("season_xp", s.get("xp", 0)) or 0
level = 1 + xp // (200 + 100 * (s.get("prestige") or 0))
print(json.dumps({"player": s.get("player"), "xp": s.get("xp"), "level": level, "score": s.get("score"),
                  "trees": trees, "counts": s.get("counts"), "log": s.get("log")}, indent=1))
print("PROBLEMS:", problems or "none")
