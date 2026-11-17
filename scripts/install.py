#!/usr/bin/env python3
"""Install zstack (vendored pstack skills contained inside it) into
~/.agents/skills, and seed personal config skeletons under ~/.zstack.

Staged copy: everything is copied into a staging folder first; the
previous install is only deleted after the new one is complete, so a
failed or interrupted run never leaves a half-applied install. Vendored
skills deploy under zstack/vendor/pstack, never as top-level skills, and
legacy top-level copies from older installs are removed after the
swap."""

import os
import shutil
import sys
from pathlib import Path

VENDORED = (
    "statechart",
    "create-formal-verification-skill",
    "maintain-formal-verification-skill",
)

MODELS_SKELETON = """\
# zstack · model picks on this machine
# Fill one line per role; zstack reads this at task start. Without it the
# main thread's model plays every role and the review panel drops to one
# seat. Roles and rules: the zstack skill's models.md.
#
# default: <model>
# hardest (once per session): <model>
# trivial edits: <model>
# judgment and prose: <model>
# invariant choice: <model>
# review seat A: <model>
# review seat B (different family): <model>
# bulk sweeps: <model>
"""

TLA_SKELETON = """\
# zstack · TLA+ toolchain on this machine
# Fill in and keep; the playbooks read this for local paths.
# TLA2TOOLS = <path to tla2tools.jar>
# JAVA = <path to a Java 11+ binary>
# TS runtime = <node / bun / deno, with version>
"""


def seed(path: Path, text: str) -> None:
    if not path.exists():
        path.write_text(text, encoding="utf-8")
        print(f"seeded {path} (fill it in)")


def main() -> int:
    here = Path(__file__).resolve().parent.parent
    dest = Path.home() / ".agents" / "skills"
    zstack_home = Path.home() / ".zstack"

    dest.mkdir(parents=True, exist_ok=True)
    (zstack_home / "adapters").mkdir(parents=True, exist_ok=True)

    stage = dest / f".zstack.stage.{os.getpid()}"
    if stage.exists():
        shutil.rmtree(stage)
    try:
        shutil.copytree(here / "skills" / "zstack", stage / "zstack")
        for name in VENDORED:
            contained = stage / "zstack" / "vendor" / "pstack" / name
            shutil.copytree(here / "vendor" / "pstack" / name, contained)
            shutil.copy2(here / "vendor" / "pstack" / "LICENSE",
                         contained / "LICENSE")
        swaps = []
        try:
            for target in ("zstack",):
                final = dest / target
                if final.exists():
                    print(f"replacing existing {final}")
                    aside = dest / f".{target}.old.{os.getpid()}"
                    os.rename(final, aside)
                    swaps.append((target, aside))
                shutil.move(str(stage / target), str(final))
        except Exception:
            for target, aside in swaps:
                if aside.exists() and not (dest / target).exists():
                    os.rename(aside, dest / target)
            for _, aside in swaps:
                shutil.rmtree(aside, ignore_errors=True)
            raise
        for _, aside in swaps:
            shutil.rmtree(aside, ignore_errors=True)
        for name in VENDORED:
            legacy = dest / name
            if legacy.exists():
                print(f"removing legacy top-level {legacy} "
                      f"(vendored skills now live inside zstack/vendor)")
                try:
                    shutil.rmtree(legacy)
                except OSError as exc:
                    print(f"warning: could not remove {legacy}: {exc}")
        seed(zstack_home / "models.md", MODELS_SKELETON)
        seed(zstack_home / "tla-toolchain.md", TLA_SKELETON)
    finally:
        shutil.rmtree(stage, ignore_errors=True)

    print(f"Installed: zstack (vendored skills contained) -> {dest}/zstack")
    print("Bind a project: commit .zstack/project.md in the repo (preferred),")
    print("or copy an adapter (adapters/*.md) to ~/.zstack/adapters/<basename>.md,")
    print("basename from the origin remote URL with .git stripped.")
    print("Then name zstack in your prompt (e.g. 'zstack: <task>')")
    print("Installed skills are build outputs: edits under ~/.agents/skills/ are")
    print("lost on the next install — change the repo (or your fork) and re-run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
