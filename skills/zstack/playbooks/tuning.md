### Tuning

One measured variable at a time: performance, balance, thresholds — any
number someone can feel or measure. The veto: do not retune stable
behavior for "polish"; every accepted change is measured against the
previous tree.

1. One variable per change. Ticket per the adapter's `ticket` field,
   constrained to the single knob you may touch, with the measured delta
   that counts as a win and the gate that measures it.
2. Baseline: run the matching gate on the current tree with the
   environment pinned per the adapter's `measurements` (same seed, same
   config, same machine) so the only moving part is the knob. A gate that varies per run is not a
   measurement tool — build a fixed-environment probe instead, and say
   that probes measure while gates verify.
3. Change the one knob, rerun the identical check, compare. Explain the
   number: name what limits it and rule out that it measured something
   else.
4. Accept → one commit naming the knob and the delta. Refute → revert and
   say what the delta showed. Never stack a second knob into the same
   commit.
5. Repeat the loop as a fresh unit for the next knob.
6. What only a human can judge (feel, sound, taste) is flagged "needs
   human", never claimed as verified by numbers.

**Reply:** knob, pinned environment, before / after numbers, decision, and
the exact `file → key` that changed.
