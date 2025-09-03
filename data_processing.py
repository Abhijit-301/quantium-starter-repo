import pandas as pd
import glob

# Load all CSV files from the data folder
csv_files = glob.glob("data/*.csv")

# Read and combine all CSVs into one DataFrame
df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)

# Keep only Pink Morsels
df = df[df['product'] == 'pink morsel']

# Convert price to numeric (strip $ sign if present)
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)


# Make sure quantity is numeric
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

# Create "sales" column = quantity * price
df['sales'] = df['quantity'] * df['price']

# Select only the required fields
processed_df = df[['sales', 'date', 'region']]

# Save to a new CSV
processed_df.to_csv("data/processed_sales.csv", index=False)

print("✅ Data processing complete! File saved as data/processed_sales.csv")
