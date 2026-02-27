# Zimozi Solutions Data Engineering Assignment

## Project Overview

This project demonstrates a complete data engineering workflow:

- PostgreSQL database backup
- Gzip compression
- Upload to Amazon S3
- S3 Lifecycle Retention Policy
- Partitioned Data Lake (Year/Month/Day)
- Querying using Amazon Athena
- Cost optimization verification

---

## Architecture Flow

## Backup Architecture

PostgreSQL Database  
↓  
pg_dump / SQL Export  
↓  
Python Backup Script  
↓  
Gzip Compression  
↓  
Amazon S3 (backups/postgres/YYYY/MM/DD/)  
↓  
S3 Lifecycle Retention Policy

## Data Lake & Analytics Architecture

PostgreSQL  
↓  
CSV Export  
↓  
Partition Script (Year/Month/Day)  
↓  
Amazon S3 (Data Lake)  
↓  
Amazon Athena (Serverless SQL Query Engine)

---

## Technologies Used

- PostgreSQL
- Python
- boto3
- AWS CLI
- Amazon S3
- Amazon Athena

---

## How to Execute

### Step 1: Install Dependencies
pip install -r requirements.txt

### Step 2: Configure AWS
aws configure

### Step 3: Run Backup Script
python backup.py

### Step 4: Upload Partitioned Data
aws s3 cp partitioned_orders s3://your-bucket-name/datalake/orders/ --recursive

### Step 5: Create Athena Table and Query

MSCK REPAIR TABLE orders;

SELECT * FROM orders LIMIT 10;

---

## Retention Policy

S3 lifecycle rule added to automatically delete backup files after specified retention period.

---

## Cost Optimization

- Used AWS Free Tier
- Enabled partition pruning in Athena
- Minimal data scanned
- Verified billing after execution
- Deleted unused resources after testing

---

## Screenshots Included

- S3 Upload
- Partition Structure
- Lifecycle Policy
- Athena Query Results
- Billing Proof
