import openpyxl
import pandas as pd

# Load the workbook
workbook = openpyxl.load_workbook("LNX Master.xlsx")

# Access the worksheet named "complete list"
worksheet = workbook["complete list"]



# Convert the list of lists into a DataFrame
df = pd.read_excel(worksheet)

# Filter the DataFrame to include only rows where '4321664' exists
filtered_df = df[df.apply(lambda row: '4321664' in row.values, axis=1)]

# Display the filtered DataFrame
print(filtered_df.head(10))