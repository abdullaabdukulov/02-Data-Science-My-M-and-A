import pandas as pd
import sqlite3 as sql

def csv_to_sql(csv_file, database, table_name):
    con = sql.connect(database)
    df = pd.read_csv(csv_file)
    df.to_sql(name=table_name, con=con, index=False, if_exists='replace')
