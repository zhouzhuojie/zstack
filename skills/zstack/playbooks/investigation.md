### Investigation

A read-only question about the project: how X works, why Y is that way,
whether Z is true. No edits, no commits, no plan unless asked.

1. Restate the question and what would count as an answer.
2. Read in the adapter's truth order: code for behavior, data/config for
   numbers, gate logs for what the tests actually assert. Cite numbers as
   `file → key`, never from a design doc.
3. Bulk reading (long files, multi-file sweeps, log digs) goes to a
   subagent on the bulk-worker role per `models.md`; keep its
   one-paragraph summary, not its transcript.
4. "Why was it built this way" → `git log` the introducing commit and
   quote its message; mark anything the record does not answer as
   unanswered.
5. Verify one risky claim by running the cheapest gate that touches it,
   when such a group exists. Read-only still allows running gates.

**Reply:** direct answer first, then evidence with `path:line` cites, then
inferences labeled as such, then what could not be answered.
