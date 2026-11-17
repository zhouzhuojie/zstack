# Contributing to zstack

Everything is plain text. Skills are markdown; scripts are small and
idempotent.

- **One playbook per change.** A playbook is a contract agents follow in
  order; keep steps short, ordered, and ending in a gate.
- **Keep vendored content pinned.** `vendor/pstack/` is upstream code at a
  pinned commit. Never hand-edit it; re-vendor at a new commit and update
  the pinned SHA in [NOTICE](NOTICE).
- **Generic means generic.** No project paths inside `skills/zstack/`, and
  no real project's paths, commands, or doc names under `adapters/` —
  examples only. Real bindings live in the target repo's
  `.zstack/project.md` or on the user's machine in `~/.zstack/adapters/`,
  never in this repo.
- **English for dev-facing text**, matching the rest of this repo.
- **Prove changes with a run.** If you touch the TLA+ stack, run one
  corpus spec end-to-end and paste the TLC output in the PR.

License: MIT. By contributing you agree your contributions are licensed
under the project license.
