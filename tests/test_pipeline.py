import pandas as pd


def test_customers():
    df = pd.read_csv("data/raw/customers.csv")

    assert len(df) > 0
    assert df["customer_id"].notna().all()
    assert df["customer_id"].is_unique


def test_bookings():
    df = pd.read_csv("data/raw/bookings.csv")

    assert len(df) > 0
    assert df["booking_id"].notna().all()
    assert df["booking_id"].is_unique
    assert df["amount"].notna().all()
    assert (df["amount"] > 0).all()


def test_destinations():
    df = pd.read_csv("data/raw/destinations.csv")

    assert len(df) > 0
    assert df["destination_id"].is_unique
    assert df["price_per_day"].notna().all()
    assert (df["price_per_day"] > 0).all()


def test_confirmed_bookings():
    df = pd.read_csv("data/curated/confirmed_bookings.csv")

    assert len(df) > 0
    assert (df["status"] == "confirmed").all()