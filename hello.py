import pandas as pd

customers = pd.read_csv("data/raw/customers.csv")

print(customers.head())
print(customers.shape)
customers.info()
