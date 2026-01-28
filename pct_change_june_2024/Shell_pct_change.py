import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Clean data
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = df["Shell (GBP)"].str.replace("£", "").astype(float)

# Get prices on required dates
price_3_june = df.loc[df["Date"] == "2024-06-03", "Close"].values[0]
price_20_june = df.loc[df["Date"] == "2024-06-20", "Close"].values[0]

# Percentage change
percentage_change = ((price_20_june - price_3_june) / price_3_june) * 100

print(round(percentage_change, 2))