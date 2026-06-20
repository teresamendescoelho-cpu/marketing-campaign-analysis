import pandas as pd

df = pd.read_csv("campaign_data.csv")

df["Conversion Rate"] = (
    df["Conversions"] / df["Clicks"]
) * 100

print(df)

best_campaign = df.loc[
    df["Conversion Rate"].idxmax()
]

print("\nBest Campaign:")
print(best_campaign)
