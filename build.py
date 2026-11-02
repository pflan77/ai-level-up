"""Build the standalone dashboard and the Claude skill package.

Usage: python3 build.py

- dashboard/dashboard.src.html + dashboard/vendor/d3 -> dashboard.html (one file, no external requests)
- copies the prompt, field guide and dashboard into skill/ai-level-up/
- rebuilds ai-level-up-skill.zip
"""
import pathlib
import shutil
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "dashboard" / "dashboard.src.html"
D3 = ROOT / "dashboard" / "vendor" / "d3.v7.9.0.min.js"
TAG = '<script src="vendor/d3.v7.9.0.min.js"></script>'
SKILL = ROOT / "skill" / "ai-level-up"

src = SRC.read_text(encoding="utf-8")
if TAG not in src:
    raise SystemExit(f"D3 script tag not found in {SRC.name}")
d3 = D3.read_text(encoding="utf-8")
if "</script" in d3.lower():
    raise SystemExit("D3 bundle contains </script and can't be inlined")
out = src.replace(TAG, "<script>\n" + d3 + "\n</script>")
(ROOT / "dashboard.html").write_text(out, encoding="utf-8")

shutil.copyfile(ROOT / "dashboard.html", SKILL / "assets" / "dashboard.html")
shutil.copyfile(ROOT / "AI_LEVEL_UP_PROMPT.md", SKILL / "references" / "rules.md")
shutil.copyfile(ROOT / "MAXIMIZATION.md", SKILL / "references" / "maximization.md")

zpath = ROOT / "ai-level-up-skill.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(SKILL.rglob("*")):
        if f.is_file() and f.name != ".DS_Store":
            z.write(f, f.relative_to(SKILL.parent))

print(f"dashboard.html {len(out.encode()) // 1024} KB · skill synced · {zpath.name} rebuilt")
