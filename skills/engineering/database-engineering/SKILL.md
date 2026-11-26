---
name: database-engineering
description: Design PostgreSQL schemas, safe migrations and efficient SQL.
---

# database-engineering

1. Inspect schema and constraints using read-only development credentials; never access production without explicit authorization.
2. Model primary/foreign keys, uniqueness, nullability, tenant boundaries and transaction invariants.
3. Parameterize queries, use transaction boundaries and explain query plans in a safe environment. EXPLAIN ANALYZE executes statements: restrict to safe test data and queries.
4. Write versioned migrations with rollback/forward recovery, test on a disposable database and check lock duration and data loss risk.
5. Test concurrency, integrity and indexes against representative data. No destructive SQL without approval and verified backups.
