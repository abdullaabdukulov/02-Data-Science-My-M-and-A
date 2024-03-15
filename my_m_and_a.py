import pandas as pd
import re
import sqlite3 as sql
from my_ds_babel import *


def clean_data(data):
    data['Country'] = "USA"
    data['City'] = data['City'].apply(lambda x: " ".join(re.findall("[a-zA-Z]+", str(x).title())))
    data['Email'] = data['Email'].apply(lambda x: str(x).lower() if not pd.isna(x) else "None")
    data['Email'] = data['Email'].apply(lambda x: x + ".in" if x.endswith('@woodinc') else x)
    data['Gender'] = data['Gender'].apply(lambda x: 'Male' if x in ['M', '0', 'Male'] else 'Female')

    data['FirstName'] = data['FirstName'].apply(lambda x: " ".join(re.findall("[a-zA-Z]+", str(x).title())))
    data['LastName'] = data['LastName'].apply(lambda x: " ".join(re.findall("[a-zA-Z]+", str(x).title())))
    data['Age'] = data['Age'].apply(lambda x: int("".join(re.findall("\d+", str(x)))) if not pd.isna(x) else None)
    data['Age'] = data['Age'].astype(str)

    return data


def my_m_and_a(df1, df2, df3):
    table1 = pd.read_csv(df1).drop(['UserName'], axis=1)
    data1 = clean_data(table1)

    table2 = pd.read_csv(df2, delimiter=';', header=None)
    table2.rename(columns={0: 'Age', 1: 'City', 2: 'Gender', 4: 'Email', 3: 'Name'}, inplace=True)
    table2['FirstName'] = table2['Name'].apply(lambda x: x.split()[0])
    table2['LastName'] = table2['Name'].apply(lambda x: x.split()[1])
    table2['Country'] = "USA"
    table2 = table2[['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country']]
    data2 = clean_data(table2)

    table3 = pd.read_csv(df3, delimiter='\t', skiprows=1, header=None)
    table3.rename(columns={0: 'Gender', 1: 'Name', 2: 'Email', 3: 'Age', 4: 'City', 5: 'Country'}, inplace=True)
    table3['FirstName'] = table3['Name'].apply(lambda x: x.split()[0])
    table3['LastName'] = table3['Name'].apply(lambda x: x.split()[1])
    table3 = table3[['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country']]
    data3 = clean_data(table3)

    full_data = pd.concat([data1, data2, data3], ignore_index=True)
    return full_data