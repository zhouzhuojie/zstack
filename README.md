# zstack

A coding-agent workflow you summon with one line — `use zstack to fix
this` — that routes the task to a playbook, follows it step by step, and
does not claim done until your project's own verification gate is green.

zstack is a localization of Poteto's pstack for everyday use: plain skill
folders, any model provider, any repo with a test gate.

## Quick start

1. **Install** — copies the skill to `~/.agents/skills/zstack/`, with the
   vendored pstack skills contained inside it (never as separate global
   skills):

   ```sh
   scripts/install.sh      # macOS / Linux / Git Bash on Windows
   scripts/install.ps1     # PowerShell on Windows
   ```

   The installed copy is a build output: local edits under
   `~/.agents/skills/` are lost on the next install — change the repo (or
   your fork) and re-run.

2. **Bind a project** (once per repo) — commit `.zstack/project.md`, or
   copy an example from `adapters/` to `~/.zstack/adapters/<basename>.md`
   (`basename` = the repo's origin remote with `.git` stripped). No
   adapter? zstack drafts one from your `AGENTS.md` / CI config and
   labels it "draft, unverified" — it never invents a gate command
   silently.

3. **Use it**:

   ```
   use zstack to fix the flaky checkout test — repro first, then fix
   use zstack to add three config presets
   use zstack to draw the login/session state machine so I can see it
   use zstack to prove that save→load never duplicates user settings
   ```

Naming zstack is the whole trigger — no slash menu, no plugin. `use
zstack to …` works in every harness; OpenCode (including T3 Code) also
accepts `@zstack <task>`.

## What happens when you send that

1. zstack resolves the project **adapter**: the gate command, the
   what-change → what-to-run table, the ticket format, language and
   branch rules.
2. It matches the task to one of eight **playbooks** and follows the
   steps in order, saying which step it is on.
3. Each role — implementer, reviewers, bulk readers — runs on a model you
   picked: the roles are defined in `skills/zstack/models.md`, your picks
   live in `~/.zstack/models.md` (the installer seeds it; fill it from
   your provider's model list).
4. It ends in your **gate** and pastes the PASS lines as the evidence for
   "done".

## The eight playbooks

| Playbook | Use it when |
|---|---|
| `investigation` | a read-only question: how does X work, why, are we sure |
| `bug-fix` | something is broken, or the gate is red — reproduce first |
| `data-add` | new content: entries, config values, copy — data only |
| `tuning` | one measured variable at a time; before/after evidence decides |
| `feature` | new behavior in code — ticket, sketch, gate, review |
| `statechart` | "show me this state machine", rule breaks as shortest paths |
| `property-test` | prove an invariant tests can't reach; sabotage-checked |
| `shipping` | land it: broad gate green, docs in the present tense, hand-off |

## What zstack adds over pstack

The rigor — reproduce first, smallest change, prove-it-works,
cross-family review — and the TLA+ machinery come from pstack, vendored
unchanged at a pinned commit. What zstack changes:

| pstack | zstack |
|---|---|
| ~44 skills, subagent wrappers, per-harness setup | one router, eight playbooks, two small config files |
| a fixed multi-vendor model lineup | roles, not brands — point them at any provider's models |
| generates a verification skill when a project has none | assumes your project already has a gate, and routes every step into it |
| an operating mode you keep enabled | explicit by name: fires when you say zstack, never silently |
| Cursor-first, ported elsewhere | plain `SKILL.md` folders, verified in OpenCode, a layout any harness can read |

In one line: **pstack is an operating style; zstack is a thin router that
keeps the rigor and drops the setup.**

## The TLA+ stack

`statechart` writes a small TLA+ model of a state machine, checks every
reachable state with TLC, and hands back a Mermaid chart labeled in the
reader's words, each rule break shown as a shortest path. Every claimed
bug must be replayed against the real code before it counts.

`property-test` verifies one invariant the normal tests can't reach —
TLA+ for bad step orders, generated inputs inside your gate for
real-code behavior — and leaves a recheck behind. Its core rule: a check
you've never seen fail proves nothing, so each property is
sabotage-tested once before it is trusted.

Setup for any machine: `skills/zstack/tla-toolchain.md` — two env vars,
no admin install.

## Repo layout

| Path | What it is |
|---|---|
| `skills/zstack/` | the router, the playbooks, model-role and toolchain config |
| `adapters/` | example project bindings — generic, no real-repo specifics |
| `vendor/pstack/` | pstack's statechart + formal-verification skills, pinned; deployed inside the zstack skill |
| `scripts/` | installers and `validate.py`, run in CI |

## License & credits

MIT — see [LICENSE](LICENSE).

zstack adapts workflow concepts from, and vendors parts of,
[pstack](https://github.com/backnotprop/pstack) by Lauren "Poteto" Tan
(MIT), itself a standalone mirror of
[cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack).
Vendored at commit `f2772d528dc1f9f24bfba17d4e9f280db86857ae`
(upstream 0.15.43): `statechart`,
`create-formal-verification-skill`, and
`maintain-formal-verification-skill`, each under its own MIT license.
Full attribution: [NOTICE](NOTICE).

Status: early; built for personal use first, preparing for a public
release.
