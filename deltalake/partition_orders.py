import pandas as pd
import os

# Read exported CSV
df = pd.read_csv("orders.csv")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Extract partitions
df["year"] = df["order_date"].dt.strftime("%Y")
df["month"] = df["order_date"].dt.strftime("%m")
df["day"] = df["order_date"].dt.strftime("%d")

base_path = "partitioned_orders"

for (year, month, day), group in df.groupby(["year", "month", "day"]):
    path = f"{base_path}/year={year}/month={month}/day={day}"
    os.makedirs(path, exist_ok=True)
    group.drop(columns=["year", "month", "day"]).to_csv(f"{path}/orders.csv", index=False)

print("Partitioning complete.")