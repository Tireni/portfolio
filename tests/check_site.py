"""Smoke checks for generated, résumé-aligned portfolio."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"content.json").read_text(encoding="utf-8"))
dist=ROOT/"dist"
index=(dist/"index.html").read_text(encoding="utf-8")
assert len(d["projects"])==3
assert [p["name"] for p in d["projects"]]==["Daynote","Career Booster","BANT"]
for text in ["Enoch Benson","Baze University","December 2026","Freelance Mobile App Developer","2019","Daynote","Career Booster","BANT","Firebase","Paystack","thebantapp.vercel.app","profile-photo","project-grid"]:
    assert text in index,text
for unwanted in ["2TOC Solutions","BOOSTAR","N-Alerts","NFDRC","NFEC","Technical Lead"]:
    assert unwanted not in index,unwanted
assert (dist/"assets/resume-portfolio.css").exists()
assert (dist/"assets/style.css").exists()
for name in ["daynote","career-booster","bant"]:
    page=dist/"case-studies"/f"{name}.html"
    assert page.exists(),name
    html=page.read_text(encoding="utf-8")
    assert 'href="../assets/style.css"' in html
    assert 'href="../index.html#work"' in html
assert 'src="https://avatars.githubusercontent.com/u/35170595?v=4"' in index
assert index.count('class="project-card new-project-card"')==3
print("Portfolio build tests passed: scoped content, profile image, project pages and visual assets.")
