
import sqlite3


def csv_to_sql(my_m_and_a, database, table_name):
    engine = sqlite3.connect(database)
    my_m_and_a.to_sql(name=table_name, con=engine, if_exists='replace')
    engine.commit()
    engine.close()
    print("Successfully converted:)")