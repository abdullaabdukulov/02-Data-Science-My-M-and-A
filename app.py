import pandas as pd
import sqlite3

def load_dataset_1(path):
    return pd.read_csv(path)


def load_dataset_2(path):
    return pd.read_csv(path, delimiter=';', names=["Age", "City", "Gender", "FullName", "Email"])


def load_dataset_3(path):
    return pd.read_csv(path, sep="\t", names=pd.read_csv(path).columns)[1:]


def cleaner(row):
    if 'string_' in row:
        row = row[7:]
    if 'integer_' in row:
        row = row[8:]
    if 'boolean_' in row:
        row = row[8:]
    if 'character_' in row:
        row = row[10:]
    if 'year' in row:
        row = row[:-4]
    return row


def clean_gender_1(row):
    if row == '0' or row == 'M':
        row = "Male"
    elif row == '1' or row == 'F':
        row = "Female"
    return row


def clean_dataset_1(df):
    df['Gender'] = df['Gender'].apply(clean_gender_1)
    df['FirstName'] = df['FirstName'].str.title().replace(r'\\', '', regex=True).replace(r'"', '',
                                                                                         regex=True).str.title()
    df['LastName'] = df['LastName'].str.title().replace(r'\\', '', regex=True).replace(r'"', '',
                                                                                       regex=True).str.title() + ' ' + \
                     df['FirstName']
    df['UserName'] = df['UserName'].str.lower()
    df['Email'] = df['Email'].apply(lambda row: row.lower() + '.com' if row[-4:].lower() != '.com' else row.lower())
    df['City'] = df['City'].str.title()
    df['Country'] = 'USA'
    return df


def clean_dataset_2(df):
    df['City'] = df['City'].str.title()
    df['Gender'] = df['Gender'].apply(clean_gender_1)
    df["FullName"] = df["FullName"].str.title().replace(r'\\', '', regex=True).replace(r'"', '', regex=True)
    df["FirstName"] = df["FullName"].apply(lambda x: x.split()[0])
    df['LastName'] = df["FullName"].apply(lambda x: x.split()[-1])
    df.drop("FullName", axis=1, inplace=True)
    df['Country'] = 'USA'
    df['Email'] = df['Email'].str.lower()
    return df


def clean_dataset_3(df):
    # df['Gender'] = df['Gender'].str.replace('string_', '', regex=True).replace('boolean_', '', regex=True).replace('character_', '', regex=True)
    df['Gender'] = df['Gender'].apply(cleaner).apply(clean_gender_1)
    df['Name'] = df['Name'].apply(cleaner).str.title().replace(r'"', '', regex=True)
    df["FirstName"] = df["Name"].apply(lambda x: x.split()[0])
    df['LastName'] = df["Name"].apply(lambda x: x.split()[-1])
    df.drop("Name", axis=1, inplace=True)
    df['Email'] = df['Email'].str.replace('string_', '', regex=True)
    df["Age"] = df["Age"].apply(cleaner)
    df['City'] = df['City'].apply(cleaner).str.title()
    df['Country'] = "USA"
    return df


def my_m_and_a(data_path_1, data_path_2, data_path_3):
    df_1 = load_dataset_1(data_path_1)
    df_2 = load_dataset_2(data_path_2)
    df_3 = load_dataset_3(data_path_3)

    clean_df_1 = clean_dataset_1(df_1)
    # print(clean_df_1)

    clean_df_2 = clean_dataset_2(df_2)
    # print(clean_df_2)

    clean_df_3 = clean_dataset_3(df_3)
    # print(clean_df_3)

    merged_df = pd.concat([clean_df_1, clean_df_2, clean_df_3], ignore_index=True)
    return merged_df

data_path_1 = "only_wood_customer_us_1.csv"
data_path_2 = "only_wood_customer_us_2.csv"
data_path_3 = "only_wood_customer_us_3.csv"


def csv_to_sql(csv_content, database, table_name):
    df = pd.read_csv(csv_content)
    engine = sqlite3.connect(database)
    df.to_sql(name=table_name, con=engine, if_exists='replace')
    print("Successfully converted:)")

merged_csv = my_m_and_a(data_path_1, data_path_2, data_path_3)
merged_csv.to_csv("merged_dataset.csv", index=False)
csv_to_sql("merged_dataset.csv", 'plastic_free_boutique.db', 'customers')

