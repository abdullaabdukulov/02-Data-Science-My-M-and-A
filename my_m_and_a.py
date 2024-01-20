import pandas as pd
import my_ds_babel
import warnings
warnings.filterwarnings('ignore')

def my_m_and_a(dt1, dt2, td3):
    
    all_dt1 = pd.read_csv(dt1)
    all_dt2 = pd.read_csv(dt2, sep=';', header=None, names=['age', 'city', 'gender', 'name', 'email'])
    all_td3 = pd.read_csv(td3, sep='\t', skiprows=1, names=['gender', 'name', 'email', 'age', 'city', 'country'])


    genders = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
    all_dt1['Gender'] = all_dt1['Gender'].replace(genders)
    all_dt1['FirstName'] = all_dt1['FirstName'].replace(r'\W', '', regex=True)
    all_dt1['FirstName'] = all_dt1['FirstName'].str.title()
    all_dt1['LastName'] = all_dt1['LastName'].replace(r'\W', '', regex=True)
    all_dt1['LastName'] = all_dt1['LastName'].str.title()
    all_dt1['Email'] = all_dt1['Email'].str.lower()
    all_dt1['City'] = all_dt1['City'].str.replace('_', '-')
    all_dt1['City'] = all_dt1['City'].str.title()
    all_dt1['Country'] = 'USA'
    all_dt1.drop('UserName', axis=1, inplace=True)


    all_dt2.age = all_dt2.age.str.replace(r'\D', '',  regex=True)
    all_dt2.city = all_dt2.city.str.replace("_", '-').str.title()
    genders = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
    all_dt2['gender'] = all_dt2['gender'].replace(genders)
    all_dt2.name = all_dt2.name.str.title()
    name_df = all_dt2.name.str.split(expand=True)
    all_dt2['first_name'], all_dt2['last_name'] = name_df[0], name_df[1]
    all_dt2.first_name = all_dt2.first_name.str.replace('\W', '').str.title()
    all_dt2.last_name = all_dt2.last_name.str.replace("\W", "").str.title()
    all_dt2.drop('name', axis=1, inplace=True)
    all_dt2['Country'] = 'USA'
    all_dt2['email'] = all_dt2['email'].str.lower()
    all_dt2 = all_dt2[['gender', 'first_name', 'last_name', 'email', 'age', 'city',  'Country']]
    all_dt2.rename(columns={'gender': 'Gender', 'first_name':'FirstName', 'last_name':'LastName', 'email':'Email', 'age':'Age', 'city':'City', 'Country':'Country',},inplace=True )


    all_td3.replace(r'string_', '', regex=True, inplace=True)
    all_td3.replace(r'boolean_', '',regex=True, inplace=True)
    all_td3.replace(r'character_', '', regex=True, inplace=True)
    all_td3['gender'] = all_td3['gender'].replace(genders)
    all_td3.replace(r'integer_', '', regex=True, inplace=True)
    all_td3['email'] = all_td3['email'].str.lower()
    all_td3.age = all_td3.age.str.replace("\D", "", regex=True)
    all_td3.city = all_td3.city.str.replace("string_", "").str.replace("_", "-").str.title()
    nw = all_td3['name'].str.split(expand=True)
    all_td3['first_name'] = nw[0]
    all_td3['last_name'] = nw[1]
    all_td3.first_name = all_td3.first_name.str.replace('\W', '' )
    all_td3.last_name = all_td3.last_name.str.replace("\W","" ).str.title()
    all_td3.first_name = all_td3.first_name.str.replace('string_', '' ).str.title()
    all_td3['country'] = 'USA'
    all_td3.drop('name', axis=1, inplace=True)
    all_td3 = all_td3[['gender', 'first_name', 'last_name', 'email', 'age', 'city', 'country']]
    all_td3.rename(columns={'gender': 'Gender', 'first_name':'FirstName', 'last_name':'LastName', 'email':'Email', 'age':'Age', 'city':'City', 'country':'Country',},inplace=True )
    
    
    dt1 = pd.concat([all_dt1, all_dt1, all_dt1], ignore_index=True)
    dt1 = dt1.astype('string')


    dt1.LastName = dt1.LastName.astype("str")
    dt1.FirstName = dt1.FirstName.astype("str")
    dt1.Gender = dt1.Gender.astype("str")

    return dt1