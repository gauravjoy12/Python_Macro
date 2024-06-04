import sqlite3

db_path = "workflow_database.db"  # Change this to your desired database path

conn = sqlite3.connect(db_path)
conn.close()

print("Database file created successfully.")
