import pandas as pd

# Define the workbook path and the output folder
#workbook_path = "C:\\Users\\X250380\\OneDrive - MerckGroup\\Desktop\\SoPo Macro\\Macro_file_1.xlsm"
output_folder = "C:\Dump\new_Task"


# Define the file names of the reports you want to read
file1 = output_folder + "LNX Master.xlsx"

df1 = pd.read_excel(file1,sheet_name="complete list")
rslt_df = df1.loc[df1['Sold_To'] == 49829180]
print(rslt_df)
print(df1)



