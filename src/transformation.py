import pandas as pd

customers = pd.read_csv("data/raw/customers.csv")
bookings = pd.read_csv("data/raw/bookings.csv")
destinations = pd.read_csv("data/raw/destinations.csv")

transformed = bookings.merge(
    customers,
    on="customer_id",
    how="left"
)

transformed = transformed.merge(
    destinations,
    on="destination",
    how="left"
)

transformed["booking_date"] = pd.to_datetime(transformed["booking_date"])

transformed["booking_year"] = transformed["booking_date"].dt.year
transformed["booking_month"] = transformed["booking_date"].dt.month

transformed.to_csv(
    "data/processed/travel_bookings.csv",
    index=False
)

print("Transformation completed successfully!")
print(transformed)