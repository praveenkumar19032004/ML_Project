import pandas as pd

# Student dataset
data = {
    "ID": [101, 102, 103, 103, 104],
    "Name": ["Arun", "Priya", None, None, "Kavin"],
    "Marks": [85, 92, 78, 78, None]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Dataset statistics
print("\nStatistics:")
print(df.describe())

print("\nCleaned Dataset:")
print(df)
