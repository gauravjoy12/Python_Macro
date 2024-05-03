# importing sql library
import pandas as pd
from sqlalchemy import create_engine

#convert excel file to data frame 
excel_file = "C:\Users\X250380\OneDrive - MerckGroup\Desktop\SoPo Macro\Input File\ " # Replace "your_excel_file.xlsx" with the path to your Excel file
df = pd.read_excel(excel_file, sheet_name="Lookup Tool",)
print(df)
# create a reference
# for sql library
engine = create_engine('sqlite://',
					echo=False)

# attach the data frame to the sql
# with a name of the table

df.to_sql('Pending sale order',
			con=engine)

# show the complete data
# from Employee_Data table
print(engine.execute("SELECT * FROM LNX Master").fetchall())
