Backup Approaches

Approach 1: pg_dump + S3 Storage

Use pg_dump
Compress using gzip
Upload to Amazon S3
Use lifecycle policy for retention

Cost:
S3 storage only
No compute cost
Cheapest long-term

Restore Speed:
Fast (direct restore using psql)
Operational Complexity:
Low

Approach 2: Full Database Snapshot (Conceptual)

Take filesystem snapshot
Store full copy in S3

Cost:
Higher storage usage
Larger restore time

Restore Speed:
Slower than logical backup
Operational Complexity:
Higher

Retention Approaches

S3 Lifecycle Policy

Script-based deletion

Cheapest Long Term:
S3 lifecycle policy

Fastest Restore:
Recent compressed pg_dump backup

Followed Approach:
pg_dump + S3 + Lifecycle