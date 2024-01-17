import pandas as pd 
import re
import my_ds_babel


def my_m_and_a(csv_1, csv_2, csv_3):
    
    csv_1 = pd.read_csv('only_wood_customer_us_1.csv')
    csv_2 = pd.read_csv('only_wood_customer_us_2.csv', sep=';', header=None, names=['Age', 'City', 'Gender', 'firstname_lastname', 'Email'])
    csv_3 = pd.read_csv('only_wood_customer_us_3.csv', sep='\t', skiprows=1, names=['Gender', 'firstname_lastname', 'Email', 'Age', 'City', 'Country'] )
    

    csv_1.fillna('string_None', inplace=True)
    csv_2.fillna('string_None', inplace=True)
    csv_3.fillna('string_None', inplace=True)

    csv_1['firstname_lastname'] = csv_1['FirstName'] + csv_1['LastName']

    csv_3['Gender'] = csv_3['Gender'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['firstname_lastname'] = csv_3['firstname_lastname'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['Email'] = csv_3['Email'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['Age'] = csv_3['Age'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['City'] = csv_3['City'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['Country'] = csv_3['Country'].map(lambda x: re.search('_(.*)', x).group(1))

    csv_4 = pd.concat([csv_1, csv_2, csv_3])

    csv_4.drop(['FirstName', 'LastName', 'UserName', 'Country'], axis=1, inplace=True) # We discard incomplete and unnecessary columns.

    gen = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
    csv_4['Gender'] = csv_4['Gender'].replace(gen)
    
    return csv_4.to_csv(index=False)