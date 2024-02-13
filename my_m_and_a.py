import pandas as pd
from tabulate import tabulate
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data_1 = BASE_DIR + '/only_wood_customer_us_1.csv'
data_2 = BASE_DIR + '/only_wood_customer_us_2.csv'
data_3 = BASE_DIR + '/only_wood_customer_us_3.csv'

def load_dataset_1(path):
    return pd.read_csv(path)

def load_dataset_2(path):
    return pd.read_csv(path, delimiter=';', names=["Age", "City", "Gender", "FullName", "Email"])

def load_dataset_3(path):
    return pd.read_csv(path, sep="\t", names=["Gender", "Name", "Email", "Age", "City", "Country"])[1:]

def pretty_print(df):
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

def clean_gender(row):
    if row=='0' or row=='M':
        row = "Male"
    elif row=='1' or row=='F':
        row = "Female"
    return row

def cleaning_string_integer_3(df):
    return df.applymap(lambda x: x.replace("string_", "").replace("boolean_", "").replace("integer_", ""))

def clean_dataset_1(df):
    df['Gender'] = df['Gender'].apply(clean_gender)
    df['FirstName'] = df['FirstName'].apply(lambda x: x.replace("\\", "").replace('"', "").title() if isinstance(x, str) else x)
    df['LastName'] = df['LastName'].apply(lambda x: x.replace("\\", "").replace('"', ""))
    df['UserName'] = df['UserName'].str.lower()
    df['Email'] = df['Email'].apply(lambda row: row.lower()+'.com' if row[-4:].lower()!='.com' else row.lower())
    df['City'] = df['City'].apply(lambda x: x.replace("_", " ").replace('-', " ")).str.title()
    df['Country'] = 'USA'
    return df

def clean_dataset_2(df):
    df["Age"] = df["Age"].apply(lambda x: x.replace("year", "").replace("years", ""))
    df["City"] = df["City"].apply(lambda x: x.replace("-", " ").replace("_", " ")).str.title()
    df["Gender"].replace({"0": "Male", "1": "Female", "M": "Male", "F": "Female"}, inplace=True)
    df["FullName"] = df["FullName"].apply(lambda x: x.replace("\\", "").replace('"', "")).str.title()
    df["Email"] = df["Email"].str.lower()
    df['Country'] = 'USA'

    return df
    

def clean_dataset_3(df):
    df["Gender"] = df['Gender'].replace({"string_": "", "boolean_": "", "integer_": "", "0": "Male", "1": "Female", "_": "", "Characterm": "nan"}, regex=True).str.title()
    df["Name"] = df["Name"].apply(lambda x: x.replace("string_", "").replace('"', "")).str.title()
    df["Email"] = df["Email"].astype(str).apply(lambda x: x.replace("string_", "").lower())
    df["Age"] = df["Age"].apply(lambda x: x.replace("integer_", "").replace("year", ""))
    df["City"] = df["City"].apply(lambda x: x.replace("string_", "")).str.title()
    df["Country"] = "USA"
    return df

df_1 = load_dataset_1(data_1)
df_2 = load_dataset_2(data_2)
df_3 = load_dataset_3(data_3)

clean_df_1 = clean_dataset_1(df_1)
clean_df_2 = clean_dataset_2(df_2)
clean_df_3 = clean_dataset_3(df_3)


def func():
    merged_df = pd.concat([clean_df_1, clean_df_2, clean_df_3], ignore_index=True)
    return merged_df

