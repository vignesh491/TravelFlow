import pandas as pd

customers = pd.read_csv("data/raw/customers.csv")
bookings = pd.read_csv("data/raw/bookings.csv")
destinations = pd.read_csv("data/raw/destinations.csv")

print("Customers:")
print(customers)

print("\nBookings:")
print(bookings)

print("\nDestinations:")
print(destinations)