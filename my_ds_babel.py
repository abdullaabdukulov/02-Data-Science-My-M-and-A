import sqlite3

def my_ds_babel_csv_to_sql(merged_df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    merged_df.to_sql(table_name, conn, index=False, if_exists="append")    
    conn.commit()
    conn.close()
    return merged_df
