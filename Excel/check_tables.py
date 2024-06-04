import sqlite3
import os

def check_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch the list of tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print the list of tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    conn.close()

if __name__ == "__main__":
    db_path = "workflow_database.db"  # Change this to your database path
    
    if not os.path.exists(db_path):
        print("Database file does not exist.")
    else:
        check_tables(db_path)
