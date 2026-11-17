### Feature

New or changed behavior in code. The slowest playbook — treat it that way.

1. Ticket first, per the adapter's `ticket` field, with the gate group
   named in acceptance. No acceptance criteria, no work.
2. Independent or large → a worktree, per the adapter's `branch` policy;
   record the baseline commit first. One system per change; a few files,
   not ten.
3. Read before writing: the adapter's `docs` list first; then whatever the
   change touches — state machines, registries, asset pipelines. Register
   before you draw, per the adapter's `registries`; the project's red
   tests name the rules.
4. Sketch before code: if the change crosses a function boundary, one
   short paragraph naming the caller, the data shape, and where the
   numbers will live in data/config. Then implement on the default model.
5. Verify per the adapter's `groups`: the matching group, then the broad
   gate.
6. Review the diff per the review-panel protocol in `models.md` when it
   crosses a boundary or touches risky behavior; otherwise reread it
   cold and cut slop. Build the lever: the second time this change does
   something by hand, extend the gate, the generator, or the test
   instead.
7. Small commits, each green. Follow `shipping` when done.

**Reply:** what the user can now do, where the numbers live, gate output
pasted, and what still needs human judgment.
