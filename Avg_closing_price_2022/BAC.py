import pandas as pd

df = pd.read_csv("data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# convert prices to numbers
df["BAC (CHF)"] = df["BAC (CHF)"].astype(float)


august_2022 = df[
    (df["Date"].dt.year == 2022) &
    (df["Date"].dt.month == 8)
]

average_price = august_2022["BAC (CHF)"].mean()
print(round(average_price, 2))
