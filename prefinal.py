import pandas as pd

# Assuming both files have a 'Customer_ID' column to join on
customer_transactions_path = "D:/pragnya/Bitathon/gantijob/merging/Customer transactions.xlsx"
merged_call_centers_path = "D:/pragnya/Bitathon/gantijob/merging/merged_call_centers.xlsx"

# Load the Excel files
customer_transactions = pd.read_excel(customer_transactions_path)
merged_call_centers = pd.read_excel(merged_call_centers_path)

# Merge the dataframes on 'Customer_ID' using an outer join
merged_df = pd.merge(customer_transactions, merged_call_centers, on='Customer_ID', how='outer')

# Save the merged dataframe to a new Excel file
output_path = "D:/pragnya/Bitathon/gantijob/merging/prefinal.xlsx"
merged_df.to_excel(output_path, index=False)

output_path
