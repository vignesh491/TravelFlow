import pandas as pd


def test_customers():
    df = pd.read_csv("data/raw/customers.csv")
    assert len(df) == 5
    assert df["customer_id"].is_unique


def test_bookings():
    df = pd.read_csv("data/raw/bookings.csv")
    assert len(df) == 10
    assert df["booking_id"].is_unique


def test_confirmed_bookings():
    df = pd.read_csv("data/curated/confirmed_bookings.csv")
    assert len(df) == 8
    assert (df["status"] == "confirmed").all()