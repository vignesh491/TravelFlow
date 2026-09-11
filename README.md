# TravelFlow

An end-to-end data engineering pipeline for processing and analyzing travel booking data.

## Project Overview

TravelFlow processes raw travel data through ingestion, cleaning, transformation, curation, database storage, and SQL analytics.

## Pipeline

Raw CSV Data → Ingestion → Cleaning → Transformation → Curation → SQLite → SQL Analytics

## Technologies

- Python
- Pandas
- SQL
- SQLite
- PySpark
- AWS S3
- AWS Glue
- Amazon Athena
- Git & GitHub

## Data

The project contains:

- 5 customers
- 10 bookings
- 8 destinations
- 8 confirmed bookings

## Analytics

The pipeline generates:

- Total bookings by destination
- Total revenue by destination
- Average booking amount
- Most popular destinations

## AWS Architecture

The cloud deployment design uses:

```text
Raw CSV
   ↓
Amazon S3
   ↓
AWS Glue ETL
   ↓
Processed Data
   ↓
Amazon S3
   ↓
Curated Data
   ↓
Amazon Athena
   ↓
SQL Analytics