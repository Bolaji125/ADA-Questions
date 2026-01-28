import pandas as pd

df = pd.read_csv("data.csv")

# Clean data
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = df["ASML (EUR)"].str.replace("€", "").astype(float)

df = df.sort_values("Date")

#Filter for q1
q1 = df[
    (df["Date"].dt.year == 2022) &
    (df["Date"].dt.month <= 3)
]

#Calculate daily percentage returns
q1["Daily Return (%)"] = q1["Close"].pct_change() * 100

#Calculate volatility
volatility_q1 = q1["Daily Return (%)"].std()
print(round(volatility_q1, 2))