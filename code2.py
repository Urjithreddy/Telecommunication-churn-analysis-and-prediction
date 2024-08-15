import pandas as pd
#this code removes the duplicate
# Load the dataframe
# Make sure the file path and the dataframe variable name match your actual usage
df = pd.read_excel('filtered_cities.xlsx')  # Replace with your actual file path

# Keep only the first occurrence of each city
df_filtered = df.drop_duplicates(subset='city', keep='first')

# Write the filtered dataframe to a new Excel file
df_filtered.to_excel('filtered_unique_cities.xlsx', index=False)
