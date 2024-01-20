import sqlite3
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    db_df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    db_df.to_csv('all_fault_lines.csv', index=False)
    with open('all_fault_lines.csv') as f:
        contents = f.read().strip('\n')
        data = contents.split("\n")

        print(len(data[1:]))
        return (contents)
    f.close()

def csv_to_sql(csv_content, database, table_name):
    connection = sqlite3.connect(database)
    df = pd.read_csv(csv_content)[:432]
    df.to_sql(table_name, connection, index=False)