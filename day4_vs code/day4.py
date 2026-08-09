# Step 1: Import Pandas
import pandas as pd

# Step 2: Load the student score dataset
df = pd.read_csv(r"C:\Users\Praveen kumar\student_scores_20_rows.csv")

print open("dataloaded successfully");
# Step 3: Display the first 5 rows
print(df.head())

# Step 4: Display the last 5 rows
print(df.tail())

# Step 5: Check the number of rows and columns
print("Shape of dataset:", df.shape)

# Step 6: Display column names
print("Columns:")
print(df.columns)

# Step 7: Display dataset information
print(df.info())

# Step 8: Display summary statistics
print(df.describe())

