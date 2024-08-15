import pandas as pd

# Load your dataframes here
# Assuming 'CC.xlsx' is your file containing call center data
# Assuming 'filtered_unique_cities.xlsx' is your file containing the city data
df_cc = pd.read_excel('CC.xlsx')
df_cities = pd.read_excel('filtered_unique_cities.xlsx')

# Create a set of valid city names for faster membership checking
valid_cities = set(df_cities['city'].unique())

# Function to update call center names based on city validation
def update_call_center_name(call_center):
    # Extract the city name or the first part before ' - ' if it exists
    potential_city_name = call_center.split(' - ')[0].strip()
    # Remove 'Call Center' if it's part of the name
    potential_city_name = potential_city_name.replace(' Call Center', '').strip()
    
    # Check if the extracted name is in the list of valid cities
    return potential_city_name if potential_city_name in valid_cities else None

# Apply the function to update the call_center names
df_cc['call_center'] = df_cc['call_center'].apply(update_call_center_name)

# Write the modified dataframe to a new Excel file
df_cc.to_excel('updated_call_centers.xlsx', index=False)
