#!/usr/bin/env python3
"""Validate the zstack repo. Stdlib only.

Checks: the skill's frontmatter name matches its directory; the playbook
tables in SKILL.md and README both match the playbook files; playbook
references resolve; adapters use only Step 0 contract fields (example.md
mirrors the full contract); the vendored exec bits survived; the pinned
upstream commit in NOTICE agrees with the one in README. Reads normalize
CRLF so the checks hold on autocrlf checkouts."""

import re
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skill = root / "skills" / "zstack"
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


# 1. Frontmatter: name matches the skill's directory name; description.
text = read(skill / "SKILL.md")
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
check(m is not None, "SKILL.md: no frontmatter block")
if m:
    fm = m.group(1)
    nm = re.search(r"^name:\s*(\S+)", fm, re.M)
    check(nm is not None and nm.group(1) == skill.name,
          f"SKILL.md: frontmatter name must match directory '{skill.name}'")
    check(re.search(r"^description:\s*\S", fm, re.M) is not None,
          "SKILL.md: missing description")


# 2. The playbook tables in SKILL.md and README match the files.
rows = re.findall(r"^\|[^|]+\|\s*`([a-z-]+)`\s*\|\s*$", text, re.M)
playbooks = sorted(p.stem for p in (skill / "playbooks").glob("*.md"))
check(sorted(set(rows)) == playbooks,
      f"SKILL.md playbook table {sorted(set(rows))} != files {playbooks}")
readme_rows = re.findall(r"^\|\s*`([a-z-]+)`\s*\|", read(root / "README.md"),
                         re.M)
check(sorted(set(readme_rows)) == playbooks,
      f"README playbook table {sorted(set(readme_rows))} != files {playbooks}")


# 3. Sibling references resolve.
for name in ("models.md", "tla-toolchain.md"):
    check((skill / name).is_file(), f"missing sibling file {name}")
for pb in playbooks:
    body = read(skill / "playbooks" / f"{pb}.md")
    for ref in re.findall(r"\]\((\.\./[a-z-]+\.md)\)", body):
        check((skill / "playbooks" / ref).is_file(),
              f"playbooks/{pb}.md: dangling reference {ref}")


# 4. Exec bits preserved in the git index.
need_exec = [
    "scripts/install.sh",
    "vendor/pstack/statechart/scripts/statechart",
    "vendor/pstack/statechart/scripts/test/java.ts",
]
out = subprocess.run(["git", "ls-files", "-s", *need_exec], cwd=root,
                     capture_output=True, text=True).stdout
modes = {}
for line in out.splitlines():
    parts = line.split("\t")
    if len(parts) == 2:
        modes[parts[1].strip('"')] = parts[0].split(" ")[0]
for p in need_exec:
    check(modes.get(p, "").startswith("100755"),
          f"{p}: not executable in the git index")


# 5. The pinned upstream commit: NOTICE owns it, README must agree.
notice = read(root / "NOTICE")
pin = re.search(r"[0-9a-f]{40}", notice)
check(pin is not None, "NOTICE: no 40-hex pinned upstream SHA")
if pin:
    check(pin.group(0) in read(root / "README.md"),
          "README: pinned upstream SHA disagrees with NOTICE")


# 6. Adapters use only Step 0 contract fields; example.md mirrors the
# full contract.
block = re.search(r"The adapter names:(.*?)(?:\n\n|$)", text, re.S)
check(block is not None, "SKILL.md: no 'The adapter names:' contract block")
if block:
    contract = set(re.findall(r"`([a-z][a-z -]*)`\s*\(", block.group(1)))
    adapters = sorted((root / "adapters").glob("*.md"))
    check(len(adapters) > 0, "adapters/: no example adapter")
    for ad in adapters:
        fields = {f.strip() for f in re.findall(r"^-\s*\*\*([^*]+)\*\*:",
                                                read(ad), re.M)}
        check("gate" in fields, f"{ad.name}: required field 'gate' missing")
        unknown = fields - contract
        check(not unknown,
              f"{ad.name}: fields outside the contract: {sorted(unknown)}")
        if ad.name == "example.md":
            check(fields == contract,
                  f"example.md: contract coverage mismatch: extra "
                  f"{sorted(fields - contract)}, missing "
                  f"{sorted(contract - fields)}")

if fails:
    for f in fails:
        print("FAIL:", f)
    sys.exit(1)
print("validate: OK — frontmatter, playbook tables, references, exec "
      "bits, pin agreement, adapter contract")
