import sqlite3
import pandas as pd

connection = sqlite3.connect("data/travelflow.db")

query = """
SELECT
    destination,
    COUNT(*) AS total_bookings,
    SUM(amount) AS total_revenue,
    AVG(amount) AS average_booking_amount
FROM confirmed_bookings
GROUP BY destination
ORDER BY total_revenue DESC;
"""

result = pd.read_sql(query, connection)

print("TravelFlow Analytics:")
print(result)

connection.close()