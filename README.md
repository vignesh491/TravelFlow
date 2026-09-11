# TravelFlow

TravelFlow is an end-to-end data engineering project that processes travel booking data through ingestion, cleaning, transformation, curation, database storage, and SQL analytics.

## Project Pipeline

Raw CSV Data
→ Data Ingestion
→ Data Cleaning
→ Data Transformation
→ Data Curation
→ SQLite Database
→ SQL Analytics

## Technologies

- Python
- Pandas
- SQL
- SQLite
- Git & GitHub

## Project Structure

```text
TravelFlow/
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── bookings.csv
│   │   └── destinations.csv
│   ├── processed/
│   │   └── travel_bookings.csv
│   ├── curated/
│   │   └── confirmed_bookings.csv
│   └── travelflow.db
├── src/
│   ├── ingestion.py
│   ├── cleaning.py
│   ├── transformation.py
│   ├── curation.py
│   ├── database.py
│   └── analytics.py
├── tests/
├── hello.py
├── requirements.txt
└── README.md