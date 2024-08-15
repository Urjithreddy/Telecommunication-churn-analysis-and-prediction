import pandas as pd
#Here We have removed the cities which don't have any call centres in them.
# Load the dataframes
df1 = pd.read_excel('GL.xlsx')  # Dataframe with city names
df2 = pd.read_excel('CC.xlsx')  # Dataframe with call center names

# Create a list of unique city names from df1
unique_cities = df1['city'].unique()

# Define a function to check if a call center name contains any city name
def contains_city(call_center, cities):
    call_center_parts = call_center.lower().split()  # Split the call center name into parts
    for city in cities:
        city_parts = city.lower().split()  # Split the city name into parts
        if all(part in call_center_parts for part in city_parts):
            return True
    return False

# Apply the function to each call center name, marking matches
df2['matches_city'] = df2['call_center'].apply(contains_city, cities=unique_cities)

# Filter df2 for rows where a city match was found
matched_call_centers = df2[df2['matches_city']]

# Extract city names from the matched call centers
matched_cities = matched_call_centers['call_center'].apply(lambda x: [city for city in unique_cities if contains_city(x, [city])]).explode().unique()

# Filter df1 to keep only cities that have a matching call center
filtered_cities = df1[df1['city'].isin(matched_cities)]

# Write the filtered dataframe to a new Excel file
filtered_cities.to_excel('filtered_cities.xlsx', index=False)
