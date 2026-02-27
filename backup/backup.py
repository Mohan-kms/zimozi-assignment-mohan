import os
import gzip
import shutil
import subprocess
from datetime import datetime
import boto3

BUCKET_NAME = "zimozi-mohan-2026-demo"
DB_NAME = "saasdb"
DB_USER = "postgres"

today = datetime.now()
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")

backup_filename = f"backup_{today.strftime('%Y%m%d')}.sql"
compressed_filename = backup_filename + ".gz"

subprocess.run([
    "pg_dump",
    "-U", DB_USER,
    "-F", "p",
    DB_NAME,
    "-f", backup_filename
], check=True)

with open(backup_filename, 'rb') as f_in:
    with gzip.open(compressed_filename, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

os.remove(backup_filename)

s3 = boto3.client("s3")
s3_path = f"backups/postgres/{year}/{month}/{day}/{compressed_filename}"

s3.upload_file(compressed_filename, BUCKET_NAME, s3_path)

print("Uploaded:", s3_path)

os.remove(compressed_filename)