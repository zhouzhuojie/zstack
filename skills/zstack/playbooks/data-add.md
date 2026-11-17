### Data add

New content: entries, config values, copy, assets referenced by data. Data
only: if the plan touches code, stop and ask whether the system is missing
a data-driven entry point before writing any.

1. Ticket first, per the adapter's `ticket` field, naming the target
   file and key, and the acceptance gate group.
2. Copy the shape of a neighboring entry. A key the code does not read
   does nothing; a key the schema requires turns the gate red — let the
   gate teach the schema rather than guessing.
3. User-facing strings follow the adapter's `strings` pipeline exactly;
   never hand-edit generated files when the project marks them generated.
4. Values that change what the user feels or measures additionally follow
   `tuning`'s before/after comparison rule before accepting.
5. Verify: the adapter's data gate, plus every group its `groups` table
   owes for what changed.
6. Follow `shipping` when done.

**Reply:** what was added, where the truth now lives (`file → key`), gate
output pasted.
