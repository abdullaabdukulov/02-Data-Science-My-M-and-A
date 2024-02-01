import pandas as pd
import sqlite3



def csv_to_sql(merged_csv, db_name, table_name):
    conn = sqlite3.connect(db_name)
    merged_csv.to_sql(table_name, conn, if_exists='append', index=False)
    conn.commit()
    conn.close()



# print(conn.cursor().execute("select count(Gender) from table_name;").fetchone())
