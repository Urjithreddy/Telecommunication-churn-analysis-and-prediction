import pandas as pd
#Here We have removed the cities which don't have any call centres in them.
# Load the dataframes
df1 = pd.read_excel('GL.xlsx')  # Dataframe with city names like "Miramar Beach"
df2 = pd.read_excel('CC.xlsx')  # Dataframe with call center names like "Miramar - IRU"

# Extract the first word of the call_center names
call_centers = df2['call_center'].apply(lambda x: x.split(' ')[0])

# Filter the cities in df1 for an exact match in the extracted call_centers
filtered_cities = df1[df1['city'].isin(call_centers)]

# Write the filtered dataframe to a new Excel file
filtered_cities.to_excel('filtered_cities.xlsx', index=False)
