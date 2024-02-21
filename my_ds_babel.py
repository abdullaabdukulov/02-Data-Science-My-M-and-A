import my_m_and_a
import sqlite3


def csv_to_sql(merged_data, db_name, table_name):
    conn = sqlite3.connect(db_name)
    merged_data.to_sql(table_name, conn, if_exists='replace')
    print("Successfully converted csv to sql")
    conn.close()


merged_csv = my_m_and_a.merge_data(my_m_and_a.data_1, my_m_and_a.data_2, my_m_and_a.data_3)
csv_to_sql(merged_csv, 'users.db', 'customers')
