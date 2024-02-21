import pandas as pd

path_1 = "only_wood_customer_us_1.csv"
path_2 = "only_wood_customer_us_2.csv"
path_3 = "only_wood_customer_us_3.csv"


def load_dataset_1(path):
    return pd.read_csv(path)


df_1 = load_dataset_1(path_1)


def clean_gender_1(row):
    if row == '0' or row == 'M':
        row = "Male"
    elif row == '1' or row == 'F':
        row = "Female"
    return row


def clean_dataset_1(df):
    df['Gender'] = df['Gender'].apply(clean_gender_1)
    df['FirstName'] = df['FirstName'].str.title()
    df['LastName'] = df['LastName'].str.title()
    df['UserName'] = df['UserName'].str.lower()
    df['Email'] = df['Email'].apply(lambda row: row.lower() + '.com' if row[-4:].lower() != '.com' else row.lower())
    df['City'] = df['City'].str.title()
    df['Country'] = 'USA'
    return df


data_1 = clean_dataset_1(df_1)


def load_dataset_2(path):
    return pd.read_csv(path, delimiter=";", names=["Age", "City", "Gender", "FullName", "Email"])


df_2 = load_dataset_2(path_2)


def clean_gender_2(row):
    if row == '0' or row == 'M':
        row = "Male"
    elif row == '1' or row == 'F':
        row = "Female"
    return row


def clean_email(row):
    if pd.isna(row):
        return None
    if row[-4:].lower() != '.com':
        return row.lower() + ".com"
    else:
        return row.lower()


def clean_dataset_2(df):
    df["Gender"] = df["Gender"].apply(clean_gender_2)
    df["City"] = df["City"].str.title()
    df['Email'] = df['Email'].apply(clean_email)
    df["Age"] = df["Age"].str.replace(r'[a-zA-Z]', '', regex=True)
    df['FullName'] = df['FullName'].str.replace(r'[\\"]', '', regex=True).str.title()
    df['FirstName'] = df['FullName'].str.split().str[0]
    df['LastName'] = df['FullName'].str.split().str[-1]
    # df[['FirstName', 'LastName']] = df['FullName'].str.split(' ', 1, expand=True)
    df.drop('FullName', axis=1, inplace=True)
    return df


data_2 = clean_dataset_2(df_2)


def load_dataset_3(path):
    return pd.read_csv(path, delimiter="\t", names=['Gender', 'Name', 'Email', 'Age', 'City', 'Country'])


df_3 = load_dataset_3(path_3)


def clean_gender_3(row):
    if row == '0' or row == 'M':
        row = "Male"
    elif row == '1' or row == 'F':
        row = "Female"
    return row


def clean_dataset_3(df):
    df = df.drop(0)
    df["Gender"] = df["Gender"].str.replace(r'^string_|^boolean_|^character_', '', regex=True)
    df["Gender"] = df["Gender"].apply(clean_gender_3)
    df["Name"] = df["Name"].str.replace(r'^string_|"', '', regex=True).str.title()
    df['FirstName'] = df['Name'].str.split().str[0]
    df['LastName'] = df['Name'].str.split().str[-1]
    df.drop('Name', axis=1, inplace=True)
    df["Email"] = df["Email"].str.replace(r'^string_', '', regex=True).str.lower()
    df["Age"] = df["Age"].str.replace(r'[a-zA-Z_]', '', regex=True)
    df["City"] = df["City"].str.replace(r'^string_', '', regex=True).str.title()
    df["Country"] = 'USA'
    return df


data_3 = clean_dataset_3(df_3)


def merge_data(data_1, data_2, data_3):
    merged_df = pd.concat([data_1, data_2, data_3], ignore_index=True)
    return merged_df
