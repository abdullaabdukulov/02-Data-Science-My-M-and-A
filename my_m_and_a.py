import pandas as pd
import my_ds_babel# Import the provided module


def cleaning_first_df(df1):
    genders_df = {'1': 'Female', '0': 'Male', 'M': 'Male', 'F':'Female'}
    df1['Gender'].replace(genders_df, inplace=True)
    
    df1['FirstName'] = df1['FirstName'].str.replace(r'(\"|\\)', '', regex=True)
    df1['FirstName'] = df1['FirstName'].str.capitalize()
    
    df1['LastName'] = df1['LastName'].str.replace(r'(\"|\\)', '', regex=True)
    df1['LastName'] = df1['LastName'].str.capitalize()
    df1['Email'] = df1['Email'].str.lower()
    df1['Age'] = df1['Age'].astype(str)
    df1['City'] = df1['City'].str.replace('-', ' ')
    df1['City'] = df1['City'].str.replace('_', ' ')
    df1['City'] = df1['City'].str.title()
    df1['Country'] = 'USA'
    df1.drop('username', axis=1, inplace=True)
    df1.dropna(inplace=True)
    
    return df1
    

def cleaning_second_df(df2):
    
    genders_df = {'1': 'Female', '0': 'Male', 'M': 'Male', 'F':'Female'}
    df2['Age'] = df2['Age'].str.replace(r'\D', '', regex=True)
    df2['name'] = df2['name'].str.replace(r'\"', '', regex=True)
    df2['name'] = df2['name'].str.replace(r'\\', '', regex=True)
    df2['name'] = df2['name'].str.title()
    
    df2[['FirstName', 'LastName']] = df2['name'].str.split(' ', expand=True)
    df2 = df2.drop('name', axis=1)
    
    df2['City'] = df2['City'].str.replace('-', ' ')
    df2['City'] = df2['City'].str.replace('_', ' ')
    df2[['FirstName', 'LastName', 'City']] = df2[['FirstName', 'LastName', 'City']].apply(lambda x: x.str.title())
    
    # Replace numeric values with corresponding Country names
    df2['Country'] = 'USA'
    df2['Gender'].replace(genders_df, inplace=True)
    df2['Email'] = df2['Email'].str.lower()
    df2.dropna(inplace=True)
    
    return df2


def cleaning_third_df(df3):
    
    genders_df = {'1': 'Female', '0': 'Male', 'M': 'Male', 'F':'Female'}
    df3['Gender'] = df3['Gender'].replace(r'string_', '', regex=True)
    df3['Gender'] = df3['Gender'].replace(r'boolean_', '', regex=True)
    df3['Gender'] = df3['Gender'].replace(r'integer_', '', regex=True)
    df3['Gender'] = df3['Gender'].replace(r'character_', '', regex=True)
    df3['Gender'] = df3['Gender'].replace(genders_df)
    df3['name'] = df3['name'].str.title()
    df3[['FirstName', 'LastName']] = df3['name'].str.split(' ', expand=True)
    df3 = df3.drop('name', axis=1)
    df3['LastName'] = df3['LastName'].str.replace('"', '')
    df3['Age'] = df3['Age'].str.replace(r'\D', '', regex=True)
    df3['City'] = df3['City'].str.replace('-', ' ')
    df3['City'] = df3['City'].str.replace('_', ' ')
    cities = {'Diego': 'San Diego', 'York': 'New York', 'Angeles': 'Los Angeles', 'Jose': 'San Jose', 'Worth': 'Fort Worth', 'Antonio': 'San Antonio', 'Francisco': 'San Francisco'}
    df3['City'] = df3['City'].replace(cities)
    df3[['FirstName', 'LastName', 'City']] = df3[['FirstName', 'LastName', 'City']].apply(lambda x: x.str.title())
    df3['Email'] = df3['Email'].str.lower()
    # Replace numeric values with corresponding Country names
    df3['Country'] = 'USA'
    df3.dropna(inplace=True)
    
    return df3

def my_m_and_a(content_database_1, content_database_2, content_database_3):
    # Load CSV contents into DataFrames
    colnames_df1 = ['Gender', 'FirstName', 'LastName', 'username', 'Email', 'Age', 'City', 'Country']
    df1 = pd.read_csv(content_database_1, skiprows=1, names=colnames_df1)
    
    colnames_df2 = ['Age', 'City', 'Gender', 'name', 'Email']
    df2 = pd.read_csv(content_database_2, sep=';', header=None, names=colnames_df2)
    
    colnames_df3 = ['Gender', 'name', 'Email', 'Age', 'City', 'Country']
    df3 = pd.read_csv(content_database_3, skiprows=1, header=None, names=colnames_df3, sep='\t')
    
    #To clean df1
    df_1 = cleaning_first_df(df1)
    
    df_2 = cleaning_second_df(df2)
    df_3 = cleaning_third_df(df3)
    
    # print(df_1[100:120])
    # print(" df1", type(df_1))
    # print(" df2", type(df_2))
    # print(" df3", type(df_3))
    # Merge the three DataFrames
    merged_df = pd.concat([df_1, df_2, df_3], ignore_index=True)
    # merged_df['Age'] = merged_df['Age'].astype(str)
    # column_nam = ["Gender", "FirstName", "LastName", "Email", "Age", "City", "Country"]
    # merged_df = merged_df.reindex(columns=column_nam)
    # merged_df.drop('Country', axis=1, inplace=True)
    # Convert the merged DataFrame to CSV format
    # merged_csv = merged_df.to_csv('merged.csv', index=False)
    # print(merged_df[merged_df['City'].str.isalpha()==False])
    
    return merged_df

# Example usage
# content_database_1 = "only_wood_customer_us_1.csv"
# content_database_2 = "only_wood_customer_us_2.csv"
# content_database_3 = "only_wood_customer_us_3.csv"

# merged_df = my_m_and_a(content_database_1, content_database_2, content_database_3)
# my_ds_babel.csv_to_sql(merged_df, 'plastic_free_boutique.sql', 'customers')
