import pandas as pd

df = pd.read_csv("data/processed/travel_bookings.csv")

confirmed = df[df["status"] == "confirmed"].copy()

confirmed.to_csv(
    "data/curated/confirmed_bookings.csv",
    index=False
)

print("Curation completed successfully!")
print(confirmed)