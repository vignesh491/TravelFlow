import pandas as pd

customers = pd.read_csv("data/raw/customers.csv")
bookings = pd.read_csv("data/raw/bookings.csv")
destinations = pd.read_csv("data/raw/destinations.csv")

customers = customers.drop_duplicates()
bookings = bookings.drop_duplicates()
destinations = destinations.drop_duplicates()

customers = customers.dropna()
bookings = bookings.dropna()
destinations = destinations.dropna()

print("Customers after cleaning:")
print(customers)

print("\nBookings after cleaning:")
print(bookings)

print("\nDestinations after cleaning:")
print(destinations)