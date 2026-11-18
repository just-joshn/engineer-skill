import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "eng-mode"
DOCUMENTS = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md")),
             *sorted(SKILL.rglob("*.md")), ROOT / "evals" / "README.md"]
SKILL_TEXT = (SKILL / "SKILL.md").read_text()

# Transcribed from the Six-State Engineering Flowchart: (source, edge label, target).
FLOWCHART = {
    ("Goal, constraints, and acceptance checks", None, "Choose playbook; investigate and design"),
    ("Choose playbook; investigate and design", None, "Implement and clean"),
    ("Implement and clean", None, "Verify actual behavior"),
    ("Verify actual behavior", None, "Evidence"),
    ("Evidence", "Correctable failure", "Choose playbook; investigate and design"),
    ("Evidence", "Verified", "Authorized endpoint"),
    ("Evidence", "Blocked or inconclusive", "Report limits and remaining work"),
    ("Authorized endpoint", "Handoff", "Deliver artifact and evidence"),
    ("Authorized endpoint", "Merge", "Meet independent shipping gates"),
    ("Meet independent shipping gates", None, "Merge and confirm actual state"),
    ("Meet independent shipping gates", "Gate cannot be met", "Report limits and remaining work"),
}

STATES = {
    "Plan": (
        ["Goal, constraints, and acceptance checks", "Choose playbook; investigate and design"],
        ["/eng-mode coordination", "task framing", "planning"],
        ["goal framing", "constraint analysis", "acceptance criteria", "scoping"]),
    "Design": (
        ["Choose playbook; investigate and design", "Correctable failure"],
        ["investigation", "design", "comparison"],
        ["investigation", "system design", "option comparison", "decision-making"]),
    "Build": (
        ["Implement and clean", "Deliver artifact and evidence"],
        ["implementation", "cleanup"],
        ["coding", "refactoring", "delegation", "cleanup"]),
    "Test": (
        ["Verify actual behavior", "Evidence", "Verified"],
        ["verification", "review"],
        ["testing", "validation", "evidence collection", "review"]),
    "Deploy": (
        ["Authorized endpoint", "Handoff", "Merge", "Deliver artifact and evidence",
         "Meet independent shipping gates", "Merge and confirm actual state"],
        ["merge", "shipping/release"],
        ["release management", "gate checks", "authorization", "rollout confirmation"]),
    "Maintain": (
        ["Meet independent shipping gates", "Blocked or inconclusive", "Gate cannot be met",
         "Report limits and remaining work"],
        ["follow-up", "remediation", "reporting"],
        ["monitoring", "issue triage", "documenting limits", "remaining-work reporting"]),
}


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def parse_metadata(text):
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise ValueError("SKILL.md needs frontmatter")
    fields = {}
    for line in match[1].splitlines():
        key, separator, raw = line.partition(":")
        if not separator or not re.fullmatch(r"[a-z-]+", key) or key in fields:
            raise ValueError("Frontmatter needs unique scalar keys")
        value = json.loads(raw)
        if not isinstance(value, str):
            raise ValueError("Use double-quoted string values in skill frontmatter")
        fields[key] = value
    return fields


class PackageTests(unittest.TestCase):
    def test_skill_frontmatter(self):
        fields = parse_metadata((SKILL / "SKILL.md").read_text())
        self.assertEqual(fields.get("name"), SKILL.name)
        self.assertRegex(fields["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(fields["name"]), 64)
        self.assertTrue(fields.get("description"))
        self.assertLessEqual(len(fields["description"]), 1024)

    def test_metadata_rejects_malformed_or_unsupported_values(self):
        for body in [
            'name: "eng-mode"\ndescription: Own a task. Use when: invoked.',
            'name: "eng-mode"\nname: "duplicate"',
            'name: "eng-mode"\ndescription: null',
            'name: "eng-mode"\ndescription: "unclosed',
        ]:
            with self.subTest(body=body), self.assertRaises(ValueError):
                parse_metadata(f"---\n{body}\n---\n")

    def test_metadata_preserves_quoted_colons(self):
        self.assertEqual(
            parse_metadata('---\nname: "eng-mode"\ndescription: "Use when: invoked"\n---\n'),
            {"name": "eng-mode", "description": "Use when: invoked"},
        )

    def test_local_document_links(self):
        for document in DOCUMENTS:
            self.assertTrue(document.is_file(), str(document))
            for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", document.read_text()):
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    path = (document.parent / unquote(url.path)).resolve()
                    self.assertTrue(path.is_relative_to(ROOT), "Link leaves the package")
                    self.assertTrue(path.is_file(), f"Missing document: {path}")
                    self.assertFalse(url.fragment, "Add anchor validation before using fragments")

    def test_standalone_skill_has_no_harness_dependencies(self):
        for document in SKILL.rglob("*.md"):
            text = document.read_text()
            with self.subTest(document=document.relative_to(SKILL)):
                self.assertNotRegex(text, r"\b(?:pi_spawn|tmux_run|ExtensionAPI)\b|@earendil-works/|/skill:")
                for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
                    url = urlsplit(target)
                    if not url.scheme and not url.netloc:
                        path = (document.parent / unquote(url.path)).resolve()
                        self.assertTrue(path.is_relative_to(SKILL), "Standalone skill links outside its bundle")

    def test_flowchart_graph(self):
        block = re.search(r"```mermaid\nflowchart TD\n(.*?)```", SKILL_TEXT, re.DOTALL)
        self.assertIsNotNone(block, "SKILL.md needs the mermaid flowchart")
        labels, edges = {}, set()
        for line in block[1].strip().splitlines():
            match = re.fullmatch(
                r'\s*(\w+)(?:\["([^"]+)"\])? (?:-->|-- "([^"]+)" -->) (\w+)(?:\["([^"]+)"\])?', line)
            self.assertIsNotNone(match, f"Unparsed flowchart line: {line}")
            source, source_label, edge, target, target_label = match.groups()
            for node, label in ((source, source_label), (target, target_label)):
                if label is not None:
                    self.assertEqual(labels.setdefault(node, label), label)
            edges.add((source, edge, target))
        self.assertEqual({(labels[s], e, labels[t]) for s, e, t in edges}, FLOWCHART)

    def test_state_table(self):
        rows = re.findall(r"(?m)^\| (Plan|Design|Build|Test|Deploy|Maintain) \| (.+) \| (.+) \| (.+) \|$",
                          SKILL_TEXT)
        self.assertEqual([row[0] for row in rows], list(STATES))
        for state, nodes, playbooks, skills in rows:
            expected_nodes, expected_playbooks, expected_skills = STATES[state]
            with self.subTest(state=state):
                self.assertEqual(re.findall(r"`([^`]+)`", nodes), expected_nodes)
                for cell, expected, folder in ((playbooks, expected_playbooks, "playbooks"),
                                               (skills, expected_skills, "skills")):
                    links = [re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", item).groups()
                             for item in cell.split("; ")]
                    self.assertEqual([name for name, _ in links], expected)
                    for name, path in links:
                        if path != "SKILL.md":
                            self.assertEqual(path, f"{folder}/{slug(name)}.md")
                            text = (SKILL / path).read_text()
                            self.assertIn(f"State: {state}.", text)
                            if folder == "playbooks":
                                self.assertRegex(text, r"(?m)^1\. ", "A playbook needs executable steps")

    def test_every_playbook_and_skill_file_is_charted(self):
        for folder, column in (("playbooks", 1), ("skills", 2)):
            charted = [f"{folder}/{slug(name)}.md" for entry in STATES.values()
                       for name in entry[column] if name != "/eng-mode coordination"]
            files = sorted(str(path.relative_to(SKILL)) for path in (SKILL / folder).glob("*.md"))
            self.assertEqual(sorted(charted), files)

    def test_node_sections_follow_the_flowchart(self):
        headings = re.findall(r"(?m)^### (.+)$", SKILL_TEXT.split("## Nodes", 1)[1].split("\n## ", 1)[0])
        nodes = {label for source, _, target in FLOWCHART for label in (source, target)}
        self.assertEqual(sorted(headings), sorted(nodes))
        for source, edge, target in FLOWCHART:
            if edge is not None:
                self.assertIn(f"- `{edge}` → `{target}`", SKILL_TEXT)

    def test_package_resources(self):
        manifest = json.loads((ROOT / "package.json").read_text())
        self.assertIn("pi-package", manifest["keywords"])
        for resource in ("skills", "prompts"):
            self.assertTrue(manifest["pi"][resource])
            for relative in manifest["pi"][resource]:
                path = (ROOT / relative).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_dir(), relative)
        self.assertIn("./eng-mode", manifest["pi"]["skills"])
        self.assertIn("./prompts", manifest["pi"]["prompts"])
        template = (ROOT / "prompts" / "eng-mode.md").read_text()
        self.assertRegex(template, r"\A---\ndescription: .+\n")
        self.assertNotIn("$@", template, "Never forward requests through lossy template arguments")
        self.assertNotIn("$ARGUMENTS", template)
        self.assertIn("/skill:eng-mode", template)
        self.assertEqual(manifest["pi"]["extensions"], ["./extensions/eng-mode.ts"])
        self.assertTrue((ROOT / manifest["pi"]["extensions"][0]).is_file())

    def test_behavior_scenario_definitions(self):
        cases = json.loads((ROOT / "evals" / "cases.json").read_text())
        self.assertTrue(cases)
        self.assertEqual(len(cases), len({case["id"] for case in cases}))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["prompt"])
                self.assertTrue(case["required"])
                self.assertTrue(all(isinstance(item, str) and item for item in case["required"]))
                if case["fixture"] is not None:
                    path = (ROOT / "evals" / case["fixture"]).resolve()
                    self.assertTrue(path.is_relative_to(ROOT / "evals"))
                    self.assertTrue(path.is_dir())


if __name__ == "__main__":
    unittest.main()
