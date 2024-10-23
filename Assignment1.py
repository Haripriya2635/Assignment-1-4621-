import os
import pandas as pd

# Load the dataset into df
data_path = os.path.join(os.getcwd(), 'Assignment1Data_Sample (1).csv')
df = pd.read_csv(data_path)
print(df.head())  # Check if dataset loaded successfully

# Create a new DataFrame with relevant columns
relevant_columns = ['Object ID', 'Department', 'Object Name', 'Title', 'Culture', 
                    'Artist Nationality', 'Object Begin Date', 'Object End Date', 
                    'Medium', 'Credit Line', 'Country']
df_cleaned = df[relevant_columns]

# Step 4: Identify duplicate Object IDs
duplicate_ids = df_cleaned[df_cleaned.duplicated(subset='Object ID', keep=False)]
print("Duplicate Object IDs:")
print(duplicate_ids)

# Remove duplicate Object IDs, keeping the first occurrence
df_cleaned = df_cleaned.drop_duplicates(subset='Object ID', keep='first')

# Step 5: Convert date columns to datetime format
df_cleaned['Object Begin Date'] = pd.to_datetime(df_cleaned['Object Begin Date'], errors='coerce')
df_cleaned['Object End Date'] = pd.to_datetime(df_cleaned['Object End Date'], errors='coerce')

# Step 7: Identify invalid dates (where Object End Date < Object Begin Date)
invalid_dates = df_cleaned[df_cleaned['Object End Date'] < df_cleaned['Object Begin Date']]

# Print invalid entries
print("Invalid Date Entries:")
print(invalid_dates)

# Remove invalid entries
df_cleaned = df_cleaned[df_cleaned['Object End Date'] >= df_cleaned['Object Begin Date']]

# Print updated shape to confirm invalid dates are removed
print("Updated shape of the cleaned dataset after removing invalid dates:")
print(df_cleaned.shape)


print("Cleaned dataset exported to 'cleaned_dataset.csv'")
