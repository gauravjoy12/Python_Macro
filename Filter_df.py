import pandas as pd

# Read the Excel file into a DataFrame from the second sheet
excel_file = "LNX Master.xlsx"  # Replace "your_excel_file.xlsx" with the path to your Excel file
excel_file_2 = "Purple Product Lookup Tool_v4.12.xlsb"  # Replace "your_excel_file.xlsx" with the path to your Excel file

df = pd.read_excel(excel_file_2, sheet_name="Lookup Tool")
print(df)
# Take input from user to filter the DataFrame
user_input = 50199776
# Filter the DataFrame based on user input
filtered_df = df.loc[df['Sold To'] == user_input] 
# Specify the specific columns to 

#columns_to_display = ['Sold To', 'SPA Cluster', 'Customer Name','Account Type', 'Regional/SPA']  


# Display matched records
if not filtered_df.empty:
    print("Matched records:")
    print(filtered_df)
    
else:
    print("No matching records found.")
