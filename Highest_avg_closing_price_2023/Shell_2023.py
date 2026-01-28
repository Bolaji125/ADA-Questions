import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Clean data
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = df["Shell (GBP)"].str.replace("£", "").astype(float)

# Filter for 2023
df_2023 = df[df["Date"].dt.year == 2023]

# Create Month column
df_2023["Month"] = df_2023["Date"].dt.to_period("M")

# Calculate average closing price per month
monthly_avg = df_2023.groupby("Month")["Close"].mean()

# Find highest month
highest_month = monthly_avg.idxmax()
highest_value = monthly_avg.max()

print("Highest Month:", highest_month, "Highest Value:", highest_value)