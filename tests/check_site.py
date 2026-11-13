"""Checks for the résumé-aligned static portfolio."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"content.json").read_text(encoding="utf-8"))
html=(ROOT/"dist/index.html").read_text(encoding="utf-8")
assert len(data["projects"]) == 3
assert [p["name"] for p in data["projects"]] == ["Daynote","Career Booster","BANT"]
for word in ["Enoch Benson","Baze University","December 2026","Freelance Mobile App Developer","2019","Daynote","Career Booster","BANT","Firebase","Paystack","thebantapp.vercel.app"]:
    assert word in html, word
for old in ["2TOC Solutions", "BOOSTAR", "N-Alerts", "NFDRC", "NFEC", "Technical Lead"]:
    assert old not in html, old
assert html.count('<section') == 4
print("Portfolio scope checks passed.")
