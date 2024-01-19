import pandas as pd 
import re
import my_ds_babel


def my_m_and_a(csv1, csv2, csv3):
    
    csv_1 = pd.read_csv(csv1)
    csv_2 = pd.read_csv(csv2, sep=';', header=None, names=['Age', 'City', 'Gender', 'firstname_lastname', 'Email'])
    csv_3 = pd.read_csv(csv3, sep='\t', skiprows=1, names=['Gender', 'firstname_lastname', 'Email', 'Age', 'City', 'Country'] )
    

    csv_1.fillna('None', inplace=True)
    csv_2.fillna('None', inplace=True)
    csv_3.fillna('string_None', inplace=True)
    
    csv_2['FirstName'] = csv_2['firstname_lastname'].map(lambda x: x.split()[0])
    csv_2['LastName'] = csv_2['firstname_lastname'].map(lambda x: x.split()[1])
    csv_3['FirstName'] = csv_3['firstname_lastname'].map(lambda x: x.split()[0])
    csv_3['LastName'] = csv_3['firstname_lastname'].map(lambda x: x.split()[1])
    csv_2.drop(['firstname_lastname'], axis=1, inplace=True)
    csv_3.drop(['firstname_lastname'], axis=1, inplace=True)


    csv_3['Gender'] = csv_3['Gender'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['FirstName'] = csv_3['FirstName'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['Email'] = csv_3['Email'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['Age'] = csv_3['Age'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['City'] = csv_3['City'].map(lambda x: re.search('_(.*)', x).group(1))
    csv_3['Country'] = csv_3['Country'].map(lambda x: re.search('_(.*)', x).group(1))

    csv_4 = pd.concat([csv_1, csv_2, csv_3])

    gen = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
    csv_4['Gender'] = csv_4['Gender'].replace(gen)
    csv_4['Country'] = 'USA'
    csv_4['UserName'] = csv_4['UserName'].fillna('Unknown')

    
    return csv_4.to_csv(index=False)