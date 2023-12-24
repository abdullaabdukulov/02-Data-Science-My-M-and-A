import pandas as pd
import sqlite3 as sql
def csv_to_sql(csv, databese, tableName):

    con = sql.connect(databese)
    df = pd.read_csv(csv)
    df.to_sql(name=tableName, con=con, index=False, if_exists='replace')




