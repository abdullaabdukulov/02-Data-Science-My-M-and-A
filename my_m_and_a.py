import pandas as pd
import csv
import sqlite3 as sql
from my_ds_babel import csv_to_sql


gender = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
elems = {'"': '', r'\\': '', 'boolean_': '', 'integer_': '', 'year': '', 'character_': '', 'eger_': ''}


def filter_data(df):
    df.replace(elems, regex=True, inplace=True)
    df.replace(gender, inplace=True)
    df.replace('"', '', regex=True, inplace=True)
    df.replace(r"\\", '', regex=True, inplace=True)
    df.replace('years', '', regex=True, inplace=True)

    df['City'] = df['City'].map(lambda x: x.capitalize())
    df['Email'] = df['Email'].map(lambda x: x.lower())
    df['LastName'] = df['LastName'].map(lambda x: x.capitalize())
    df['FirstName'] = df['FirstName'].map(lambda x: str(x).capitalize())
    df['Country'] = df['Country'].map(lambda x: 'U.S.A')
    df['Age'] = df['Age'].map(lambda x: str(x)[:2])
    df['UserName'] = df['FirstName'].map(lambda x: x.lower())

    return df


def filter_content_1(csv_file):
    df = pd.read_csv(csv_file)
    return filter_data(df)


def filter_content_2(csv_file):
    with open(csv_file, 'r') as csvfile:
        data = {
            'Gender': list(),
            'FirstName': list(),
            'LastName': list(),
            'UserName': list(),
            'Email': list(),
            'Age': list(),
            'City': list(),
            'Country': list()
        }
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            data['Gender'].append(row[2])
            data['FirstName'].append(row[3].split(' ')[0])
            data['LastName'].append(row[3].split(' ')[1])
            data['UserName'].append(row[3].split(' ')[0])
            data['Email'].append(row[-1])
            data['Age'].append(row[0])
            data['City'].append(row[1].capitalize())
            data['Country'].append('U.S.A')

        df = pd.DataFrame.from_dict(data, orient='columns')
        return filter_data(df)


def filter_content_3(csv_file):
    with open(csv_file, 'r') as csvfile:
        data = dict()

        csvreader = csv.reader(csvfile, delimiter='\t')
        for row in csvreader:
            if not data:
                splited = row[0].split(',')
                for key in splited:
                    data[key] = list()
                data['FirstName'] = data.pop('Name')
                data['LastName'] = list()
            else:
                data['Gender'].append(row[0].strip('string_'))
                data['FirstName'].append(row[1].strip('string_').split(' ')[0])
                data['LastName'].append(row[1].strip('string_').split(' ')[1])
                data['Email'].append(row[2].strip('string_'))
                data['Age'].append(row[3].strip('string_'))
                data['City'].append(row[4].strip('string_'))
                data['Country'].append(row[-1])

        df = pd.DataFrame.from_dict(data, orient='columns')
        return filter_data(df)


def merge_data(df1, df2, df3):
    frames = [df1, df2, df3]
    df = pd.concat(frames, ignore_index=True)
    df.to_csv('merged.csv', index=False)


def csv_to_sql(csv, database, table_name):
    con = sql.connect(database)
    df = pd.read_csv(csv)
    df.to_sql(name=table_name, con=con, index=False, if_exists='replace')


def my_m_and_a(content1, content2, content3):
    cleaned_data_1 = filter_content_1(content1)
    cleaned_data_2 = filter_content_2(content2)
    cleaned_data_3 = filter_content_3(content3)

    merge_data(cleaned_data_1, cleaned_data_2, cleaned_data_3)

    csv_to_sql('merged.csv', 'plastic_free_boutique.sql', 'customers')

my_m_and_a('only_wood_customer_us_1.csv',
           'only_wood_customer_us_2.csv',
           'only_wood_customer_us_3.csv')
