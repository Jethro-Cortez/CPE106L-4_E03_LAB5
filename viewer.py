import os
import sqlite3
from prettytable import PrettyTable

def list_db_files():
    db_files = [f for f in os.listdir() if f.endswith('.db')]
    return db_files

def select_db_file(db_files):
    if len(db_files) == 1:
        return db_files[0]
    else:
        print("Select a database file:")
        for i, file in enumerate(db_files):
            print(f"{i + 1}. {file}")
        choice = int(input("Enter the number of the database file: "))
        return db_files[choice - 1]

def connect_to_db(db_file):
    conn = sqlite3.connect(db_file)
    print(f"Connected to {db_file}")
    return conn

def display_table_contents(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]
    
    table = PrettyTable()
    table.field_names = columns
    
    for row in rows:
        table.add_row(row)
    
    print(table)

def main():
    db_files = list_db_files()
    if not db_files:
        print("No database files found.")
        return
    
    selected_db = select_db_file(db_files)
    conn = connect_to_db(selected_db)
    
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("Tables in the database:")
    for i, table in enumerate(tables):
        print(f"{i + 1}. {table[0]}")
    
    for i, table in enumerate(tables):
        print(f"\nContents of table {table[0]}:")
        display_table_contents(cursor, table[0])
    
    conn.close()

if __name__ == "__main__":
    main()