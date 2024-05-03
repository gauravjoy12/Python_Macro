import pandas as pd

# Read the Excel file into a DataFrame from the second sheet
excel_file = "LNX Master.xlsx"  # Replace "your_excel_file.xlsx" with the path to your Excel file
excel_file_2 = "Purple Product Lookup Tool_v4.12.xlsb"  # Replace "your_excel_file.xlsx" with the path to your Excel file

df = pd.read_excel(excel_file_2, sheet_name="Lookup Tool",)
df = df.fillna(method='ffill', axis=0,)
#df= df.replace("", None).ffill()


print(df)
 
