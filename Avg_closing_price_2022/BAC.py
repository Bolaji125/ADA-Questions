import pandas as pd

df = pd.read_csv("data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# convert prices to numbers
df["BAC (CHF)"] = df["BAC (CHF)"].astype(float)

# Example exchange rate (student must justify source)
CHF_TO_GBP = 0.95

# Convert prices to GBP
df["BAC_GBP"] = df["BAC (CHF)"] * CHF_TO_GBP

august_2022 = df[
    (df["Date"].dt.year == 2022) &
    (df["Date"].dt.month == 8)
]

average_price_gbp = august_2022["BAC_GBP"].mean()
print(round(average_price_gbp, 2))
