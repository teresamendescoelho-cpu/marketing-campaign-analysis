import pandas as pd

data = {
    "Campaign": ["A", "B", "C"],
    "Clicks": [1200, 800, 1500],
    "Conversions": [60, 25, 90]
}

df = pd.DataFrame(data)

df["Conversion Rate"] = df["Conversions"] / df["Clicks"] * 100

print(df)
