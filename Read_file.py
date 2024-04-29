import openpyxl
import pandas as pd

# Load the workbook
workbook = openpyxl.load_workbook("LNX Master.xlsx")

# Access the worksheet named "Complete list"
worksheet = workbook["complete list"]

# Load data into a list of lists
data = []
for row in worksheet.iter_rows(values_only=True):
    data.append(row)

# Convert the list of lists into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
