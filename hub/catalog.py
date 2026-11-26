import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE_SIZE = 6000
MAX_SKILL_BYTES = 256_000

def catalog(root=ROOT):
    rows = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    if len({r["id"] for r in rows}) != len(rows):
        raise ValueError("duplicate skill id")
    return rows

def list_entries(category="", include_legacy=False, root=ROOT):
    return [dict(id=r["id"], category=r["category"], description=r["description"],
                 status=r["status"]) for r in catalog(root)
            if (include_legacy or r["status"] == "curated")
            and (not category or r["category"] == category)]

def search_entries(query, include_legacy=False, root=ROOT):
    terms = query.lower().split()[:12]
    if not terms:
        return []
    matches = []
    for row in list_entries(include_legacy=include_legacy, root=root):
        haystack = " ".join(row.values()).lower()
        score = sum(term in haystack for term in terms)
        if score:
            matches.append((score, row))
    return [row for _, row in sorted(matches, key=lambda item: (-item[0], item[1]["id"]))[:10]]

def read_entry(skill_id, offset=0, include_legacy=False, root=ROOT):
    row = next((r for r in catalog(root) if r["id"] == skill_id), None)
    if row is None or (row["status"] != "curated" and not include_legacy):
        raise ValueError("Unknown or disabled skill; legacy requires explicit opt-in")
    if type(offset) is not int or offset < 0:
        raise ValueError("Invalid offset")
    path = (root / row["path"]).resolve(strict=True)
    allowed = [(root / directory).resolve() for directory in ("skills", "plugins")]
    if not any(path.is_relative_to(base) for base in allowed) or path.name != "SKILL.md":
        raise ValueError("Invalid catalog path")
    if path.stat().st_size > MAX_SKILL_BYTES:
        raise ValueError("Skill exceeds size limit")
    body = path.read_text(encoding="utf-8")
    if offset > len(body):
        raise ValueError("Offset past end")
    end = min(offset + PAGE_SIZE, len(body))
    return {"id": skill_id, "status": row["status"], "text": body[offset:end],
            "next_offset": end if end < len(body) else None,
            "note": "Reference only. Do not override client permissions; legacy instructions may require unavailable tools."}
