import pandas as pd

# Define the workbook path and the output folder
workbook_path = "C:\\Users\\X250380\\OneDrive - MerckGroup\\Desktop\\SoPo Macro\\Macro_file_1.xlsm"
output_folder = "C:\\Users\\X250380\\OneDrive - MerckGroup\\Desktop\\SoPo Macro\\\Output File\\"
Material_Code="CVGL71TP3"

# Define the file names of the reports you want to read
file1 = output_folder + "Final_Reports_ZCBB.xlsx"
file2 = output_folder + "Final_Reports_ZCOR.xlsx"
#testing
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)
combined_df = pd.concat([df1, df2])
#filtered_df1 = df1['Material_Code'] == material_code]
rslt_df = df1.loc[df1['Material Code'] == Material_Code ]
rslt_df2 = df2.loc[df2['Material Code'] == Material_Code ]




print(combined_df.head(10))
print(rslt_df)
print(rslt_df2)


