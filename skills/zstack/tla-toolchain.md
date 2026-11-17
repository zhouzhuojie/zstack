# Zstack · TLA+ toolchain

The `statechart` and `property-test` playbooks run vendored pstack skills
(`statechart`, `create-formal-verification-skill`,
`maintain-formal-verification-skill`) contained inside this skill at
`vendor/pstack/` — they are never installed as top-level skills. The
runner needs Java 11+ and the TLC jar. mise is not required: set two
environment variables and the script uses them directly, skipping its
`mise install` fallback entirely.

## Any machine

- `TLA2TOOLS` → path to `tla2tools.jar`, from the TLA+ releases (asset
  name `tla2tools.jar`).
- `JAVA` → a Java 11+ binary. A portable JDK zip (e.g. Adoptium Temurin)
  works with no admin install.
- A TypeScript runtime: Node 23.6+ (or 22.18–22.x), Bun 1.1.5+, or Deno
  2.0+.

Verified run shape (PowerShell):

```powershell
$env:TLA2TOOLS = "<jar>"
$env:JAVA = "<java.exe>"
node --disable-warning=ExperimentalWarning "$HOME/.agents/skills/zstack/vendor/pstack/statechart/scripts/statechart.ts" SPEC.tla --config SPEC.cfg --out OUT_DIR
```

The `scripts/statechart` sh wrapper also works under bash variants. All
spec, config, view, chart-budget, and scratch-folder rules live in the
vendored skill's own `SKILL.md` — read it in full before the first run.

## Your machine

The installer seeds `~/.zstack/tla-toolchain.md` with a commented
skeleton; fill it once and every later run reads it for this machine's
paths.
