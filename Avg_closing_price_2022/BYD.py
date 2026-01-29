import pandas as pd

df = pd.read_csv("data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# convert prices to numbers
df["BYD (HKD)"] = df["BYD (HKD)"].astype(float)

# Example exchange rate (student must justify source)
HKD_TO_GBP = 0.09

# Convert prices to GBP
df["BYD_GBP"] = df["BYD (HKD)"] * HKD_TO_GBP

august_2022 = df[
    (df["Date"].dt.year == 2022) &
    (df["Date"].dt.month == 8)
]

average_price_gbp = august_2022["BYD_GBP"].mean()
print(round(average_price_gbp, 2))