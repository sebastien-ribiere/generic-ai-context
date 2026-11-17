import tempfile
import unittest
from pathlib import Path
from scripts.check_context import validate, REQUIRED


class ContextCheckTests(unittest.TestCase):
    def make_root(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        for name in REQUIRED:
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# placeholder\n", encoding="utf-8")
        return temporary, root

    def test_missing_file_is_reported(self):
        temporary, root = self.make_root()
        try:
            (root / "CLAUDE.md").unlink()
            self.assertTrue(any("CLAUDE.md" in error for error in validate(root)))
        finally:
            temporary.cleanup()

    def test_accepted_adr(self):
        temporary, root = self.make_root()
        try:
            (root / "docs/adr/0001-example.md").write_text(
                "# ADR-0001 — Example\n- **Status:** Accepted\n"
                "- **Date:** 2026-11-17\n- **Superseded by:** None\n"
                "## Context\nA\n## Decision\nB\n## Consequences\nC\n",
                encoding="utf-8",
            )
            self.assertEqual(validate(root), [])
        finally:
            temporary.cleanup()

    def test_invalid_state_is_rejected(self):
        temporary, root = self.make_root()
        try:
            (root / "docs/adr/0001-example.md").write_text(
                "# ADR-0001\n- **Status:** Unknown\n"
                "## Context\nA\n## Decision\nB\n## Consequences\nC\n",
                encoding="utf-8",
            )
            self.assertTrue(any("Status" in error for error in validate(root)))
        finally:
            temporary.cleanup()


if __name__ == "__main__":
    unittest.main()
