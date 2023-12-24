import numpy as np
import csv
import my_ds_babel
from io import StringIO
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")


def first_ds(param_1):
    if len(param_1.getvalue()) > len('Data/only_wood_customer_us_1.csv'):
        df_1_raw = pd.read_csv(param_1)
    else:
        df_1_raw = pd.read_csv(param_1.getvalue())
    df_1_raw.replace({'Gender':{'0':'Male', '1':'Female', 'M':'Male', 'F':'Female'}}, inplace=True)
    df_1_raw['FirstName'] = df_1_raw['FirstName'].str.title().replace('[^a-zA-Z]', '', regex=True)
    df_1_raw['LastName'] = df_1_raw['LastName'].str.title().replace('[^a-zA-Z]', '', regex=True)
    df_1_raw['Email'] = df_1_raw['Email'].str.lower()
    df_1_raw['City'] = df_1_raw['City'].str.title().replace('[^a-zA-Z]', ' ', regex=True)
    df_1_raw['Country'] = 'USA'
    df_1_raw.replace({'Email':{'forgottoask@woodinc':np.nan}}, inplace=True)
    df_1 = df_1_raw.reindex(columns=['Gender', 'FirstName', 'LastName', 'UserName', 'Email', 'Age', 'City', 'Country'])
    df_1 = df_1.astype(str)
    return df_1


def second_ds(param_1):
    column_names = ['Age', 'City', 'Gender', 'FullName', 'Email']
    if len(param_1.getvalue()) > len('Data/only_wood_customer_us_2.csv'):
        df_2_raw = pd.read_csv(param_1,  sep=';', names=column_names)
    else:
        df_2_raw = pd.read_csv(param_1.getvalue(),  sep=';', names=column_names)
    df_2_raw['Age'] = df_2_raw['Age'].replace('[^0-9]', '', regex=True)
    df_2_raw['City'] = df_2_raw['City'].str.title().replace('[^a-zA-Z]', ' ', regex=True)
    df_2_raw['Email'] = df_2_raw['Email'].str.lower()
    df_2_raw.replace({'Gender':{'0':'Male', '1':'Female', 'M':'Male', 'F':'Female'}}, inplace=True)
    df_2_raw[['FirstName', 'LastName']] = df_2_raw['FullName'].str.title().replace('[^a-zA-Z- ]', '', regex=True).str.extract(r'(\w+) (\w+)', expand=True) #.str.split(' ', 1, expand=True)
    df_2_raw.drop('FullName', inplace=True, axis=1)
    df_2_raw['UserName'] = df_2_raw['FirstName'].str.lower()
    df_2_raw['Country'] = 'USA'
    df_2 = df_2_raw.reindex(columns=['Gender', 'FirstName', 'LastName', 'UserName', 'Email', 'Age', 'City', 'Country'])
    df_2 = df_2.astype(str)
    return df_2


def third_ds(param_1):
    if len(param_1.getvalue()) > len('Data/only_wood_customer_us_3.csv'):
        filename = (param_1.getvalue()).split('\n')
        lst = []
        for row in filename:
            lst.append(row.split('\t'))
    else:
        filename = param_1.getvalue()
        lst = []
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                lst.append(row[0].split('\t'))
    lst.pop(0)
    df_3_raw = pd.DataFrame(lst, columns =['Gender', 'Name', 'Email', 'Age', 'City', 'Country'])
    df_3_raw.replace({'Gender':{'boolean_0':'Male', 'boolean_1':'Female', 'character_M':'Male', 'string_Female':'Female', 'string_Male':'Male'}}, inplace=True)
    df_3_raw['Age'] = df_3_raw['Age'].replace('[^0-9]', '', regex=True)
    df_3_raw[['FirstName', 'LastName']] = df_3_raw['Name'].str.title().replace('(^String)', '', regex=True).replace('[^a-zA-Z- ]', '', regex=True).str.extract(r'(\w+) (\w+)', expand=True)
    df_3_raw.drop('Name', inplace=True, axis=1)
    df_3_raw['City'] = df_3_raw['City'].str.title().replace('(^String)', '', regex=True).replace('[^a-zA-Z]', ' ', regex=True)
    df_3_raw['Email'] = df_3_raw['Email'].str.lower().replace('(^string.)', '', regex=True)
    df_3_raw.replace({'Email':{'n/a':np.nan}}, inplace=True)
    df_3_raw['UserName'] = df_3_raw['FirstName'].str.lower()
    df_3_raw['Country'] = 'USA'
    df_3 = df_3_raw.reindex(columns=['Gender', 'FirstName', 'LastName', 'UserName', 'Email', 'Age', 'City', 'Country'])
    df_3 = df_3.astype(str)
    return df_3


def my_m_and_a(dataset_1, dataset_2, dataset_3):
    frames = [first_ds(dataset_1), second_ds(dataset_2), third_ds(dataset_3)]
    result = pd.concat(frames)
    return pd.DataFrame(result)


if __name__ == '__main__':
    merged_csv = my_m_and_a(StringIO('Data/only_wood_customer_us_1.csv'), StringIO('Data/only_wood_customer_us_2.csv'), StringIO('/Data/only_wood_customer_us_3.csv')).to_csv(index=False)
    my_ds_babel.csv_to_sql(StringIO(merged_csv), 'plastic_free_boutique.db', 'customers')