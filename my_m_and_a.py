import pandas as pd
import io

def my_m_and_a(content_database_1, content_database_2, content_database_3):
    table_1 = pd.read_csv(content_database_1)
    table_1.drop(["UserName"], axis=1, inplace=True)
    table_1['Gender'] = table_1['Gender'].replace({'1': "Female" , '0': "Male"})
    table_1['Gender'] = table_1['Gender'].replace({'F': "Female" , 'M' : "Male"})

    table_2 = pd.read_csv(content_database_2, delimiter=';', header=None)
    table_2[['FirstName', 'LastName']] = table_2[3].str.split(' ', expand=True)
    table_2.drop(columns=[3], inplace=True)
    table_2 = table_2.reindex([2, 'FirstName', 'LastName', 4, 0, 1], axis=1)
    table_2.rename(columns={2: 'Gender', 4: 'Email', 0: 'Age', 1: 'City'}, inplace=True)
    table_2.rename(columns={2: 'Gender', 4: 'Email', 0: 'Age', 1: 'City'}, inplace=True)
    table_2['Gender'] = table_2['Gender'].replace({'1': "Female" , '0': "Male"})
    table_2['Gender'] = table_2['Gender'].replace({'F': "Female" , 'M' : "Male"})

    table_3 = pd.read_csv(content_database_3, delimiter='\\', header=None)
    table_3 = table_3.drop(0)
    table_3[['Gender', 'Name', 'Email', 'Age', 'City', 'Country']] = table_3[0].str.split('\t', expand=True)
    table_3[['FirstName','LastName']] = table_3['Name'].str.split(' ', expand=True)
    table_3 = table_3.drop(columns=['Name', 0], axis=1)
    table_3 = table_3.reindex(['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country'], axis=1)
    table_3['Gender'] = table_3['Gender'].replace(['boolean_' ,'string_', ], '' , regex=True)
    table_3['Gender'] = table_3['Gender'].replace({'0':'Male' , '1' : 'Female'})
    table_3['Gender'] = table_3['Gender'].str.replace('character_M', 'Male')
    table_3['FirstName'] = table_3['FirstName'].str.replace('string_', '')
    table_3['LastName'] = table_3['LastName'].str.replace('"', '')
    table_3['Email'] = table_3['Email'].str.replace('string_', '')
    table_3['Age'] = table_3['Age'].replace(['integer_', '""'], '' , regex=True)
    table_3['City'] = table_3['City'].str.replace('string_', '')
    table_3['Country'] = table_3['Country'].str.replace('string_', '')

    merged_df = pd.concat([table_1, table_2, table_3], ignore_index=True)
    merged_df['City'] = merged_df['City'].str.title()
    merged_df['Age'] = merged_df['Age'].astype(str)
    merged_df['FirstName'] = merged_df['FirstName'].replace(['\\\\', '""'], '' , regex=True)
    merged_df['FirstName'] = merged_df['FirstName'].astype(str) 
    merged_df['LastName'] = merged_df['LastName'].replace(['\\\\', '""'], '' , regex=True)
    merged_df['LastName'] = merged_df['LastName'].astype(str) 
    return merged_df
