### Statechart

The user needs to SEE a machine — any system that moves between states —
not read a spec. Runs the vendored pstack `statechart` skill: read
`vendor/pstack/statechart/SKILL.md` (relative to this skill's folder) in
full and follow it — spec, config, view, budget, scratch-folder, and
hand-off rules are all there. Toolchain setup:
[tla-toolchain.md](../tla-toolchain.md).

1. Name the machine and the reader. The adapter's `machines` list names
   the machines of record; without one, ask. The reader decides whether
   the behavior is right: label states with what the reader sees, never
   variable names.
2. Write the spec from the truth: code first, docs of record second.
   Where they disagree, the drift is itself a finding — say it before
   modeling.
3. Prove the chart against the gate: say which drawn transitions the
   project's own state-machine tests actually assert. The chart
   communicates; the gate stays the enforcement.
4. Replay every bug path against the real code — a probe or a test, one
   step per action. A path that does not reproduce in the real code
   means the model is wrong until shown otherwise. A replayed bug routes
   to `bug-fix`; the chart that found it goes in the report.
5. Hand off per the vendored skill's hand-off rules, plus one line per
   replayed finding in the project's own terms.

**Reply:** the chart, replayed findings, and the regenerate command.
