### Bug fix

You own this task. Be scientific: every shipped line traces to evidence
from a gate run. Belt-and-suspenders that "might help" is a hypothesis,
not a fix; it does not ship.

1. Reproduce through the gate. Pick the matching group from the adapter's
   `groups` and run it. A red group is a deterministic repro. No group
   covers the symptom → write the failing assertion into that group's test
   first (assert what the user observes, not internals), see it fail, and
   keep that test as part of the fix. The adapter's `probes` can locate a
   bug; only the gate verifies one.
2. Bisect the cause. Form hypotheses, kill them with gate runs and
   targeted reads; suspect numbers → read the data/config truth, not docs.
   When two fixes sharing one premise fail the same gate, stop and test
   the premise directly.
3. Fix the root cause with the smallest change the evidence justifies.
   Numbers change in data/config, not code. Revert anything a refuted
   hypothesis motivated.
4. Verify on the same surface: rerun the matching group, then the
   adapter's broad gate. "Inconclusive" or wrong-surface is not a pass.
5. Commits: write the failing test, watch it fail, then fix; land test and
   fix in one commit so every commit stays green — the commit message
   names the failing behavior it kills. Small commits.
6. Follow `shipping` when done.

**Reply:** what was broken, root cause, fix, how verified — with the
gate's PASS lines pasted verbatim.
