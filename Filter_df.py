import pandas as pd

# Read the Excel file into a DataFrame from the second sheet
excel_file = "LNX Master.xlsx"  # Replace "your_excel_file.xlsx" with the path to your Excel file
df = pd.read_excel(excel_file, sheet_name="complete list")
print(df)

# Take input from user to filter the DataFrame
user_input = 50199776

# Filter the DataFrame based on user input
filtered_df = df.loc[df['Sold To'] == user_input] 
# Specify the specific columns to display
columns_to_display = ['Sold To', 'SPA Cluster', 'Customer Name','Account Type', 'Regional/SPA']  # Replace with the actual column names you want to display


# Display matched records
if not filtered_df.empty:
    print("Matched records:")
    print(filtered_df[columns_to_display])

else:
    print("No matching records found.")
