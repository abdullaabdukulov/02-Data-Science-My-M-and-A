import sqlite3
import pandas as pd
import csv
from io import StringIO


def sql_to_csv(database, table_name):
    # Connect to SQLite database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Fetch data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Create CSV content
    csv_content = StringIO()
    csv_writer = csv.writer(csv_content)
    
    # Write header
    csv_writer.writerow(column_names)

    # Write data rows
    csv_writer.writerows(rows)

    # Close database connection
    conn.close()

    return csv_content.getvalue()

def csv_to_sql(csv_content1, database, table_name):
    # Connect to SQLite database
    csv_content = csv_content1.read()
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Read CSV content
    csv_reader = csv.reader(StringIO(csv_content))

    # Get column names from header
    columns = next(csv_reader)

    # Create table
    create_table_query = f"CREATE TABLE {table_name} ({', '.join(f'`{col}`' for col in columns)})"
    cursor.execute(create_table_query)

    # Insert data into the table
    for row in csv_reader:
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?']*len(row))})"
        cursor.execute(insert_query, row)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

