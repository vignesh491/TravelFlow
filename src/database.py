import sqlite3
import pandas as pd

df = pd.read_csv("data/curated/confirmed_bookings.csv")

connection = sqlite3.connect("data/travelflow.db")

df.to_sql(
    "confirmed_bookings",
    connection,
    if_exists="replace",
    index=False
)

result = pd.read_sql(
    "SELECT * FROM confirmed_bookings",
    connection
)

print("Database created successfully!")
print(result)

connection.close()