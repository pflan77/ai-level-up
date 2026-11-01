"""Scripted AI Level Up playtest against a local Ollama model.

Usage: python3 playtest.py <model> <prompt.md> <out.md>
"""
import json
import sys
import time
import urllib.request

MODEL, PROMPT_PATH, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
SYSTEM = open(PROMPT_PATH, encoding="utf-8").read()

# Player: Maria, a realtor. Includes vague claims, a plan, a premature Prestige and a duplicate claim.
TURNS = [
    "Start",
    "1. Maria\n2. Real estate: listing descriptions, client emails, social posts\n3. ChatGPT Plus, daily. Sometimes Gemini free.\n"
    "4. I built a Custom GPT that writes listing descriptions in my style. I've used it on about 30 listings since August.\n"
    "5. No, I don't teach anyone.\n6. I read it over and fix anything that sounds off.",
    "1. Projects: monthly client newsletter, listing descriptions, open-house follow-up emails\n"
    "2. 90-day goal: cut my weekly admin time in half\n3. About 3 hours a week",
    "Mission Complete: I made a newsletter with AI",
    "Mission Complete: I sent my November newsletter, drafted with ChatGPT, to 412 subscribers on Nov 3. Link: https://example.com/maria-nov",
    "Mission Complete: I sent my November newsletter to 412 subscribers on Nov 3.",
    "Mission Complete: I'm going to build an automation for open-house follow-ups next week.",
    "Prestige",
    "Maximization",
    "Save Game",
]


def chat(messages):
    body = json.dumps({
        "model": MODEL, "messages": messages, "stream": False, "think": False,
        "options": {"num_ctx": 16384, "temperature": 0.4},
    }).encode()
    req = urllib.request.Request("http://localhost:11434/api/chat", body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.load(r)["message"]["content"]


messages = [{"role": "system", "content": SYSTEM}]
with open(OUT, "w", encoding="utf-8") as f:
    f.write(f"# Playtest: {MODEL}\n\n")
    for i, turn in enumerate(TURNS, 1):
        messages.append({"role": "user", "content": turn})
        t0 = time.time()
        reply = chat(messages)
        messages.append({"role": "assistant", "content": reply})
        f.write(f"## Turn {i} — PLAYER\n\n{turn}\n\n## Turn {i} — GAME MASTER ({time.time() - t0:.0f}s)\n\n{reply}\n\n---\n\n")
        f.flush()
        print(f"turn {i} done ({time.time() - t0:.0f}s)", flush=True)
