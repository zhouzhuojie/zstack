# Zstack adapter · example

A filled example for a fictional project — replace every line when
binding a real repo. Bind by committing this file as `.zstack/project.md`
in the target repo, or copying it to `~/.zstack/adapters/<basename>.md`
(basename from the origin remote URL with `.git` stripped).

- **gate**: `make check` — the only verification command. `make check
  list` shows groups.
- **groups**: the changed-what → what-to-run table in `README.md` §
  Testing — that section is the truth, not this file.
- **broad gate**: `make check fast` after any change.
- **release gate**: `make ci` (full matrix, lint, e2e) — release tier /
  CI only.
- **probes**: one-off `scripts/probe/*.py` measure a number or capture a
  trace. A probe is never verification.
- **truth**: `src/` > `config/*.yaml` > test output > `docs/status.md` >
  other docs.
- **ticket**: goal / current state / constraints / acceptance, stated in
  the task's opening message. No acceptance criteria, no work.
- **boundary**: new settings and content are `config/*.yaml` changes;
  never hard-code values in `src/`. If content seems to need code, stop
  and ask whether a data-driven entry point is missing.
- **strings**: user-facing copy follows the project's i18n pipeline —
  extract keys first, fill translations, then run the i18n gate group.
- **machines**: user-session and checkout states, documented in
  `docs/state-machines.md`, partly enforced by the `ui` gate group.
- **measurements**: one variable per change, same seed and config, two
  trees compared before accepting any number.
- **registries**: register new routes in `src/routes.ts` and new fixed
  strings in `src/strings.ts` before using them.
- **language**: dev-facing work in English; user-facing copy stays in
  its authored language.
- **branch**: worktrees for independent work per CONTRIBUTING.md; branch
  and merge rules follow the zstack non-negotiables.
- **docs**: read `AGENTS.md`, then `README.md` §Testing, then
  `docs/status.md` before first work in a session.
