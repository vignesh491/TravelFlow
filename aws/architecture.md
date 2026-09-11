# TravelFlow AWS Architecture

## Overview

TravelFlow is designed as an end-to-end cloud data engineering pipeline using AWS services.

## Architecture

Raw CSV Data
→ Amazon S3
→ AWS Glue ETL
→ Processed Data
→ Amazon S3
→ Amazon Athena
→ SQL Analytics

## AWS Services

### Amazon S3
Used as the central data lake for storing:

- Raw travel data
- Processed data
- Curated data

### AWS Glue
Used for:

- Data cleaning
- Data transformation
- ETL processing
- Converting processed data into Parquet format

### Amazon Athena
Used for:

- Querying curated datasets
- Aggregating booking data
- Calculating revenue
- Performing analytical SQL queries

## Data Lake Structure

```text
S3 Bucket
│
├── raw/
│   ├── customers.csv
│   ├── bookings.csv
│   └── destinations.csv
│
├── processed/
│   └── travel_bookings.parquet
│
└── curated/
    └── confirmed_bookings.parquet