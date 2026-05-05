import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/raw/restaurant_sales.csv")

df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year
df["day"] = df["date"].dt.day
df["weekofyear"] = df["date"].dt.isocalendar().week

le_item = LabelEncoder()
le_day = LabelEncoder()
le_time = LabelEncoder()

df["item_name"] = le_item.fit_transform(df["item_name"])
df["day_of_week"] = le_day.fit_transform(df["day_of_week"])
df["time_slot"] = le_time.fit_transform(df["time_slot"])

df = df.drop(columns=["date"])

df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Preprocessing Completed")
print("Rows:",len(df))
