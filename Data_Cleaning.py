

import pandas as pd
df = pd.read_excel(r"C:\Users\ADMIN\Downloads\dirty_production_data.xlsx")

df["Shift"] = df["Shift"].fillna("Unknown")
df["Downtime_Minutes"] = df["Downtime_Minutes"].fillna(0)
df["Defect_Rate_%"] = df["Defect_Rate_%"].fillna(df["Defect_Rate_%"].mean())
df["Units_Produced"] = df["Units_Produced"].fillna(df["Units_Produced"].mean())

df["Production_Line"] = df["Production_Line"].str.strip().str.title()
df["Shift"] = df["Shift"].str.strip().str.title()
print(df["Production_Line"].unique())
print(df["Shift"].unique())

df["Date"] = pd.to_datetime(df["Date"], format="mixed")

df = df.drop_duplicates()

df.to_excel("Cleaned_Production_Data.xlsx", index=False)


print(df.isnull().sum())
print(df["Shift"].unique())
print(df["Production_Line"].unique())
print(df.shape)