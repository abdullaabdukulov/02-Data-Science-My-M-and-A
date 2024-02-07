from my_m_and_a import func
import sqlite3

def to_sql(merged_df):
    conn = sqlite3.connect("table.db")
    merged_df.to_sql("my_table", conn, index=False, if_exists="replace")    
    conn.commit()
    conn.close()
    return merged_df

to_sql(func())