import sqlite3
import csv
import pandas as pd 

# def sql_to_csv(database, table_name):
#   connection = sqlite3.connect(database)
#   curs = connection.cursor()
#   select = f"SELECT * FROM {table_name};"
#   request = pd.read_sql_query(select, connection)
#   request.to_csv("list_fault_lines.csv", index = False)
#   with open("list_fault_lines.csv", "r") as file:
#     all_results = file.read()
#   return all_results[:-1]
# print(sql_to_csv("all_fault_line.db", "fault_lines"))
def csv_to_sql(csv_content, database, table_name):
    for_description = []
    csv_read = pd.read_csv(csv_content)
    for_iloc = csv_read.iloc[:].values
    connected = sqlite3.connect(database)
    curs = connected.cursor()
    curs.execute(f"CREATE TABLE {table_name} ('Volcano Name', 'Country', 'Type', 'Latitude (dd)', 'Longitude (dd)', 'Elevation (m)')")
    curs.executemany("INSERT INTO volcanos VALUES (?, ?, ?, ?, ?, ?)", for_iloc)
    connected.commit()
    curs.execute(f"SELECT * FROM {table_name}")
    for i in curs.description:
        for_description.append(i)
    return for_description
    # connected = 
# print(csv_to_sql("list_volcano.csv", "list_volcano.db", "volcanos"))
    # return 
# database = "all_fault_line.db"
# connection = sqlite3.connect(database)
# curs = connection.cursor()
# select = "SELECT * FROM fault_lines;"
# request = pd.read_sql_query(select, connection)

# print(select)

# with open("list_fault_lines.csv", "r") as file:
#     all_results = file.read()
#     print(all_results)

# a = pd.read_csv('list_fault_lines.csv')
# print(a.isna())