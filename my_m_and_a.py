import pandas as pd
import re
import sqlite3 as sql
from my_ds_babel import *


def clean_data(data):
    data['Country'] = pd.Series(["USA" for i in data['Country']])
    data['City'] = pd.Series([" ".join(re.findall("[a-zA-Z]+", i.title())) for i in data['City'].tolist()])
    data['Email'] = pd.Series(["None" if str(i) == 'nan' else i.lower() for i in data['Email']])
    data['Email'] = pd.Series([i + ".in" if i.endswith('@woodinc') else str(i) for i in data['Email']])
    data['Gender'] = pd.Series(['Male' if i in ['M', '0', 'Male'] else 'Female' for i in data['Gender'].tolist()])

    data['FirstName'] = pd.Series([" ".join(re.findall("[a-zA-Z]+", str(i).title())) for i in data['FirstName'].tolist()])
    data['LastName'] = pd.Series([" ".join(re.findall("[a-zA-Z]+", str(i).title())) for i in data['LastName'].tolist()])
    data['Age'] = pd.Series([int(" ".join(re.findall("\d+", str(i)))) for i in data['Age'].tolist()])
    data['Age'] = data['Age'].astype(str) 

    return data

def my_m_and_a(df1,df2,df3):
    table1 = pd.read_csv(df1).drop(['UserName'], axis=1)
    data1 = clean_data(table1)

    table2 = pd.read_csv(df2, delimiter=';', header=None)
    table2.rename(columns = {0: 'Age', 1: 'City', 2: 'Gender', 4: 'Email'}, inplace = True)
    table2['FirstName'] = pd.Series([i.split()[0] for i in table2[3]])
    table2['LastName'] = pd.Series([i.split()[1] for i in table2[3]])
    table2['Country'] = pd.Series(["USA" for i in range(10000)])
    table2 = table2.drop([3], axis=1)[['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country']]
    data2 = clean_data(table2)

    table3 = pd.read_csv(df3, delimiter='\t', skiprows=1, header=None)
    for i in table3.columns:
        table3[i] = table3[i].str.replace("string_|character_|integer_|boolean_", '', regex=True)
    table3['FirstName'] = [i.split()[0] for i in table3[1]]
    table3['LastName'] = [i.split()[1] for i in table3[1]]
    del table3[1]
    table3.rename(columns = {0: 'Gender', 2: 'Email', 3: 'Age', 4: 'City', 5: 'Country'}, inplace = True)
    data3 = clean_data(table3)


    full_data = data1.append(data2).append(data3)
    return full_data