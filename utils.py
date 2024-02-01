import pandas as pd


def load_dataset_1(path):
    return pd.read_csv(path)


def clean_gender(row):
    if row == '0' or row == 'M':
        row = 'Male'
    elif row == '1' or row == 'F':
        row = 'Female'
    return row


def clean_dataset_1(df):
    df['Gender'] = df['Gender'].apply(clean_gender)
    df['FirstName'] = df['FirstName'].str.title()
    df['LastName'] = df['LastName'].str.title()
    df['UserName'] = df['UserName'].str.lower()
    df['Email'] = df['Email'].map(lambda row: row.lower() + '.com' if row[-4:].lower() != '.com' else row.lower())
    df['City'] = df['City'].str.title()
    df['Country'] = "USA"
    return df


def load_dataset_2(path):
    return pd.read_csv(path, delimiter=';', names=['Age', 'City', 'Gender', 'FullName', 'Email'])


def clean_gender_2(row):
    if row == '0' or row == 'M':
        row = 'Male'
    elif row == '1' or row == 'F':
        row = 'Female'
    return row


def clean_email_2(email):
    if pd.isna(email):
        return None
    if email[-4:] == '.com':
        return email.lower()
    else:
        return (email + '.com').lower()


def clean_dataset_2(df):
    filter_fullname = {'"': '', r'\\': ''}
    df['City'] = df['City'].str.title()
    df["Gender"] = df["Gender"].apply(clean_gender_2)
    df['FullName'] = df['FullName'].str.title().replace(filter_fullname, regex=True)
    df['Email'] = df['Email'].apply(clean_email_2)
    df['FirstName'] = df['FullName'].apply(lambda x: x.split()[0])
    df['LastName'] = df['FullName'].apply(lambda x: x.split()[-1])
    df.drop('FullName', axis=1, inplace=True)
    return df


def load_dataset_3(path):
    return pd.read_csv(path, delimiter="\t", names=['Gender', 'Name', 'Email', 'Age', 'City', 'Country']).drop(0,
                                                                                                               axis=0)


def clean_gender_3(row):
    if row == '0' or row == 'M' or row == 'chcM':
        row = 'Male'
    elif row == '1' or row == 'Fm':
        row = 'Female'
    return row


def clean_dataset_3(df):
    df['Gender'] = df['Gender'].str.replace(r'^string_|^boolean_|^character_', '', regex=True)
    df['Gender'] = df['Gender'].apply(clean_gender_3)
    df['Name'] = df['Name'].str.replace(r'^string_|"', '', regex=True).str.title()
    df['Email'] = df['Email'].str.replace(r'^string_', '', regex=True).str.lower()
    df['Age'] = df['Age'].str.replace(r'^integer_|[a-zA-Z]', '', regex=True)
    df['City'] = df['City'].str.replace(r'^string_', '', regex=True).str.title()
    df['Country'] = 'USA'
    df['FirstName'] = df['Name'].apply(lambda x: x.split()[0])
    df['LastName'] = df['Name'].apply(lambda x: x.split()[-1])
    df.drop('Name', axis=1, inplace=True)
    return df


def whole_dataset(df1, df2, df3):
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)
    return merged_df
