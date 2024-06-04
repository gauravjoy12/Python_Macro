import os
import pandas as pd
import sqlite3

def read_excel_files(input_folder):
    excel_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]
    dataframes = {}
    for file in excel_files:
        path = os.path.join(input_folder, file)
        dataframes[file] = pd.read_excel(path)
    return dataframes

def create_tables(dataframes, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for name, df in dataframes.items():
        # Assuming the first sheet of each workbook is to be used for table creation
        df.iloc[:0].to_sql(name=name.split('.')[0], con=conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

def upload_to_database(dataframes, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for name, df in dataframes.items():
        df.to_sql(name=name.split('.')[0], con=conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    input_folder = r"C:\Users\X250380\OneDrive - MerckGroup\Desktop\SoPo Macro\Input File"  # Change this to your input folder path
    db_path = "workflow_database.db"     # Change this to your database path
    
    if not os.path.exists(input_folder):
        print("Input folder does not exist.")
    elif not os.path.exists(db_path):
        print("Database file does not exist.")
    else:
        dataframes = read_excel_files(input_folder)
        create_tables(dataframes, db_path)
        upload_to_database(dataframes, db_path)
        print("Excel files uploaded to the database successfully.")
