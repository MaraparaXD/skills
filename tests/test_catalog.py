import json
import tempfile
import unittest
from pathlib import Path
from hub.catalog import catalog, list_entries, search_entries, read_entry, ROOT

class CatalogTests(unittest.TestCase):
    def test_catalog(self):
        rows = catalog()
        self.assertGreaterEqual(len(rows), 10)
        for row in rows:
            path = ROOT / row["path"]
            self.assertTrue(path.is_file(), row["path"])
            self.assertNotIn("archive", path.relative_to(ROOT).parts)
        self.assertEqual(len(list_entries()), 10)

    def test_search_and_read(self):
        self.assertTrue(search_entries("security"))
        entry = read_entry("secure-coding")
        self.assertIn("OWASP", entry["text"])
        self.assertIsNone(entry["next_offset"])

    def test_legacy_opt_in(self):
        with self.assertRaises(ValueError):
            read_entry("smart-explore")
        self.assertIn("AST", read_entry("smart-explore", include_legacy=True)["text"])

    def test_invalid_id_and_offset(self):
        for skill in ("../../etc/passwd", "missing"):
            with self.assertRaises(ValueError):
                read_entry(skill)
        with self.assertRaises(ValueError):
            read_entry("secure-coding", -1)

    def test_escape_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills").mkdir()
            (root / "secret").mkdir()
            (root / "secret/SKILL.md").write_text("secret")
            (root / "skills/escape").symlink_to(root / "secret", target_is_directory=True)
            (root / "catalog.json").write_text(json.dumps([{"id":"escape","category":"test",
                "status":"curated","description":"test","path":"skills/escape/SKILL.md"}]))
            with self.assertRaises(ValueError):
                read_entry("escape", root=root)

if __name__ == "__main__":
    unittest.main()
