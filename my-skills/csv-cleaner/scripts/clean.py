import pandas as pd
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)
original_len = len(df)

# Standardize column headers
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values column by column based on data type
for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].fillna("N/A")       # text columns → "N/A"
    else:
        df[col] = df[col].fillna(0)            # number columns → 0

df.to_csv(output_path, index=False)
print(f"Removed {original_len - len(df)} duplicate rows.")
print(f"Saved cleaned file to: {output_path}")