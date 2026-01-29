import pandas as pd

df = pd.read_csv("data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Remove the EUR symbol and convert prices to numbers
df["ASML (EUR)"] = df["ASML (EUR)"].str.replace("€", "").astype(float)

# Example exchange rate (student must justify source)
EUR_TO_GBP = 0.87

# Convert prices to GBP
df["ASML_GBP"] = df["ASML (EUR)"] * EUR_TO_GBP

august_2022 = df[
    (df["Date"].dt.year == 2022) &
    (df["Date"].dt.month == 8)
]

average_price_gbp = august_2022["ASML_GBP"].mean()
print(round(average_price_gbp, 2))