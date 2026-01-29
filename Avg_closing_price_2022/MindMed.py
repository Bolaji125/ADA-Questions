import pandas as pd

df = pd.read_csv("data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# convert prices to numbers
df["MindMed (JPY)"] = df["MindMed (JPY)"].astype(float)

# Example exchange rate (student must justify source)
JPY_TO_GBP = 0.0047

# Convert prices to GBP
df["MindMed_GBP"] = df["MindMed (JPY)"]* JPY_TO_GBP

august_2022 = df[
    (df["Date"].dt.year == 2022) &
    (df["Date"].dt.month == 8)
]

average_price_gbp = august_2022["MindMed_GBP"].mean()
print(round(average_price_gbp, 2))
