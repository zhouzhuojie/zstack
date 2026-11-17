# Zstack · model routing

Roles are the contract; model names are config. Fill the roles from your
provider's model list, keep two distinct families for the review seats,
and keep the bulk workers cheap. Never run the whole stack on one family
— that collapses the review panel into a mirror.

## Roles

| Role | What it needs |
|---|---|
| Default: code, content, investigation, bug hunts | your daily coder: cheap, strong, long context |
| Hardest bug hunt or subtle math, once per session | the default family at its top effort |
| Trivial mechanical edits | the default family at its lowest effort |
| Judgment and prose: design arbitration, tickets, copy | a second family you trust; usually the expensive seat, so it gets judgment and review only |
| Invariant choice and model judgment (what to prove, bounds, what a model leaves out) | the judgment seat |
| Review seat A (reads the diff cold) | the default family at top effort |
| Review seat B (second opinion) | a different family — a second family catches what the first is blind to |
| Bulk mechanical sweeps: value fills, renumbering, consistency checks | a cheap or free worker; every result passes a gate before it counts |

## Where the model names come from

1. Ask your harness which models it can reach — OpenCode's
   `opencode models` command or the `providers` section of its config;
   other harnesses have equivalents.
2. Write your picks, one line per role, in `~/.zstack/models.md` — the
   installer seeds it with a commented skeleton; zstack reads it at task
   start.
3. No pinned file? The main thread's model plays every role, and the
   review panel drops to a single seat — say so in the reply when that
   happens.

## Example provider

This stack was built and verified on **magpie**, a small local model
router that exposes a coder, a judge, and a free bulk worker as separate
families. Its live model list shows up in your harness's model listing
like any other provider — check there for what is available today.

## Rules

- Never switch a family unasked. If a slug fails to resolve, run the role
  on the default model and say so in the reply.
- Top effort is for the single hardest task of a session, not for loops
  or fan-out.
- The review panel runs seat A + seat B on the same diff. Keep only
  findings a gate run or code reading proves; fix small findings in
  place; log unproven ones as open questions, one line each.
- Subagent spawns set `model` to the role's slug; the main thread keeps
  the user's model.
