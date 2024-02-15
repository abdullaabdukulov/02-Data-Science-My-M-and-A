import sqlite3
import csv
from io import StringIO
import os

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = [column[1] for column in cursor.fetchall()]

    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    csv_content = ','.join(columns) + '\n'
    for row in rows:
        csv_content += ','.join(map(str, row)) + '\n'

    conn.close()
    
    return csv_content.rstrip('\n')

def csv_to_sql(csv_content, database, table_name):
    conn = sqlite3.connect('list_volcanos.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS volcanos
                (id integer primary key, 
                volcano text ,
                country text,
                type text,
                latitude real,
                longitude real,
                elevation real)
                ''')

    with open('list_volcano.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO volcanos (volcano, country, type, latitude, longitude, elevation) VALUES (?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5]))
    conn.commit()
    conn.close()
