# ADR Rules

Create an Architecture Decision Record only when a decision is material. Examples include:

- an architecture or data-model change;
- a new important dependency;
- a public API or security-boundary change;
- a release or migration change;
- building an important general-purpose capability instead of reusing a mature option;
- rejecting an obvious mature solution;
- a significant increase in complexity.

An ADR must state the context, constraints, options considered, decision, consequences, status, and links to evidence. Keep it short when the decision is small and deeper when the risk demands it.

Use statuses consistently:

```text
PROPOSED → ACTIVE → SUPERSEDED / ARCHIVED
```

Never silently replace an active ADR. Link the old record to the new one and explain why the change occurred.
