# Cost Analysis & Backup Strategy

## Backup Approaches Evaluated

### Approach 1: Logical Backup (pg_dump + Amazon S3)

Process:
- Use pg_dump to export PostgreSQL database
- Compress using gzip
- Upload to Amazon S3
- Apply S3 Lifecycle policy for automated retention

Cost:
- Only S3 storage cost
- No EC2 or compute cost
- Fully compatible with AWS Free Tier
- Cheapest long-term solution

Restore Speed:
- Fast restore using psql

Operational Complexity:
- Low
- Easy to automate via Python or CLI


---

### Approach 2: Full Database Snapshot (Conceptual)

Process:
- Take full filesystem snapshot of database
- Store entire data directory

Cost:
- Higher storage usage
- Larger backup size
- Not free-tier optimized

Restore Speed:
- Slower than logical backup
- Requires full snapshot restore

Operational Complexity:
- Higher
- Requires infrastructure-level control


---

## Retention Approaches Evaluated

### 1. S3 Lifecycle Policy
- Automatically deletes objects after defined days
- No manual intervention required
- No compute cost

### 2. Script-Based Deletion
- Manual or scheduled deletion via CLI
- Requires operational maintenance

Cheapest Long-Term Solution:
S3 Lifecycle Policy

Fastest Restore Strategy:
Recent compressed pg_dump backup


---

## Final Approach Implemented

- pg_dump logical backup
- Gzip compression
- S3 storage (date-based folder structure)
- Lifecycle policy for automatic retention
- Athena partitioning for analytics layer
- Full cleanup after execution to avoid charges


---

## Cost Control Measures

- Used AWS Free Tier services
- Minimized Athena data scan using partition pruning
- Enabled lifecycle retention policy
- Deleted S3 bucket after testing
- Dropped Athena table after testing
- Verified billing page after cleanup