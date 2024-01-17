import pandas as pd 
import sqlite3 as sql

def sql_to_csv(database, table_name):
    db = sql.connect(database)
    df = pd.read_sql(f"SELECT * FROM {table_name}", db)
    return df.to_csv(index=False).rstrip('\n')

def csv_to_sql(csv_content, database, table_name):
    df = pd.read_csv(csv_content)
    db = sql.connect(database)
    df.to_sql(name=table_name, con=db, index=False)