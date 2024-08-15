
import pandas as pd

# Load dataset1 and dataset2 from Excel files
# Replace 'path/to/dataset1.xlsx' and 'path/to/dataset2.xlsx' with the actual file paths
df1 = pd.read_excel("D:/pragnya/Bitathon/gantijob/merging/prefinal.xlsx")
df2 = pd.read_excel("D:/pragnya/Bitathon/gantijob/merging/Updated_CC_Data_with_Sentiment.xlsx")

# Merge the 'sentiment' column from df2 into df1 on 'customer_id'
df1 = pd.merge(df1, df2[['Customer_ID', 'Sentiment']], on='Customer_ID', how='left')

# Save the merged DataFrame back to an Excel file
# Replace 'path/to/merged_dataset.xlsx' with the desired output file path
df1.to_excel("D:/pragnya/Bitathon/gantijob/merging/final.xlsx", index=False)
