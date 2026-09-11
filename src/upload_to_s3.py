import boto3
from aws_config import S3_BUCKET, RAW_PREFIX, PROCESSED_PREFIX, CURATED_PREFIX

s3 = boto3.client("s3")

files = {
    "data/raw/customers.csv": RAW_PREFIX + "customers.csv",
    "data/raw/bookings.csv": RAW_PREFIX + "bookings.csv",
    "data/raw/destinations.csv": RAW_PREFIX + "destinations.csv",
    "data/processed/travel_bookings.csv": PROCESSED_PREFIX + "travel_bookings.csv",
    "data/curated/confirmed_bookings.csv": CURATED_PREFIX + "confirmed_bookings.csv",
}

for local_file, s3_key in files.items():
    s3.upload_file(local_file, S3_BUCKET, s3_key)
    print(f"Uploaded: {local_file} -> s3://{S3_BUCKET}/{s3_key}")

print("All files uploaded successfully!")