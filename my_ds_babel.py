import sqlite3
import csv
import pandas as pd


def sql_to_csv(database, table_name):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ' + table_name)
    result_1 = cursor.fetchall()
    header = [i[0].title().replace("_", " ") for i in cursor.description]
    l = []
    l.append(','.join(header))
    for tup in result_1:
        l.append(','.join([str(i) for i in tup]))
    final_res = "\n".join(l)
    return final_res



def csv_to_sql(csv_content, database, table_name):
    a = ['Mega Basalt Field', 'Ethiopia']
    df = pd.read_csv(csv_content)
    if database == 'list_volcanos.db':
        df = df[~df['Volcano Name'].isin(a)]
    connection = sqlite3.connect(database)
    df.to_sql(table_name, con=connection, if_exists='replace', index=False)