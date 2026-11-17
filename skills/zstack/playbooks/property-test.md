### Property test

For the case the gates cannot reach: a race, a retry, a state-machine
corner, an invariant the user must be able to trust. Verify ONE property
with the tool that fits, and leave the recheck behind. Vendored pstack
skills: read `vendor/pstack/create-formal-verification-skill/SKILL.md`
and `vendor/pstack/maintain-formal-verification-skill/SKILL.md`
(relative to this skill's folder) in full and follow them; toolchain:
[tla-toolchain.md](../tla-toolchain.md).

1. Choose the target from the code, not from convenience: the strongest
   promise where a break harms the user and the existing gates reach the
   case least. Inventory the property-style checks that already exist
   (determinism sweeps, audits, roundtrips) and build on them; do not
   duplicate a gate.
2. State the property and the harm in one plain sentence each, in the
   project's own terms. Choosing which property is a judgment call — the
   judgment seat per `models.md`.
3. Let the question choose the tool (pstack's own rule): a bad ORDER of
   steps → TLA+ + TLC over a small model, handed off through the
   `statechart` playbook, spec in a scratch folder; behavior for every
   input ON the real code → generated inputs inside an existing gate group
   (multi-seed assertion, exhaustive state×event enumeration for small
   machines, save→load roundtrip identity); must hold at every size where
   a bound is not enough → say so and stop: that is a proof, not a test,
   and needs the user's explicit go.
4. Able to fail: sabotage the guarded code once (comment out the check,
   reorder the step), watch the property go red, then revert the sabotage.
   Report what the sabotage run printed. A check never seen failing proves
   nothing.
5. Findings stay findings: if the current code breaks the property, report
   the counterexample in the project's terms and route the fix to
   `bug-fix`. Never weaken the property or the model until it passes; do
   not fix product code without the user.
6. Leave the recheck behind. A TLA+ check → generate the project-local
   verify skill per pstack's `create-formal-verification-skill`, with the
   coverage record and the sync commit, into the repo's `.agents/skills/`
   (project-local scope — see SKILL.md's Install scope section). A
   gate-based property → the gate rechecks it forever; add one coverage
   line to the doc that owns the system. When the covered code later
   changes, `maintain-formal-verification-skill` resyncs the
   verification.
7. Follow the generated skill once, as a cold agent would, on the sabotage
   from step 4. It must catch the break. A verify skill never run is a
   draft.

**Reply:** what was verified, which tool and why, the bounds and what is
left out, the finding or the pass with evidence, how to rerun it.
