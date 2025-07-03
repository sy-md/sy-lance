import pandas as pd
import json

# Read Excel file
df = pd.read_excel('W PHX INVENTORY_updated.xlsx')  # sheet_name='Sheet1' for specific sheet

# Convert to JSON
json_data = df.to_json(orient='table', indent=2)

# Save to file
with open('output.json', 'w') as f:
    f.write(json_data)

print("Excel converted to JSON successfully!")
