import pandas as pd
import sqlite3

def csv_to_sql(dataframe, database, table_name):
    conn = sqlite3.connect(database)
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()