import pandas as pd
import csv

gender = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
elems = {'"': '', '\\': ''}
def filter1(csv_file):
    df = pd.read_csv(csv_file)


    df['City'] = df['City'].map(lambda x: x.capitalize())
    df['Email'] = df['Email'].map(lambda x: x.lower())
    df['LastName'] = df['LastName'].map(lambda x: x.capitalize())
    # df['FirstName'] = df['FirstName'].map(lambda x: x.capitalize())
    df['Country'] = df['Country'].map(lambda x: 'U.S.A')
    # df['UserName'] = df['UserName'].map(lambda x: x.lower())

    df.replace(gender, inplace=True)


def filter2(csv_file):
    # df = pd.read_csv(csv_file)
    # print(df)
    with open(csv_file, 'r') as csvfile:
        data = {
            'Gender': list(),
            'FirstName': list(),
            'LastName': list(),
            'UserName': list(),
            'Email': list(),
            'Age': list(),
            'City': list(),
            'Country': list()
        }
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            data['Gender'].append(row[2])
            data['FirstName'].append(row[3].split(' ')[0])
            data['LastName'].append(row[3].split(' ')[1])
            data['UserName'].append(row[3].split(' ')[0])
            data['Email'].append(row[-1])
            data['Age'].append(row[0])
            data['City'].append(row[1].capitalize())
            data['Country'].append('U.S.A')


        df = pd.DataFrame.from_dict(data, orient='columns')

        df.replace(gender, inplace=True)
        df.replace('"', '', regex=True, inplace=True)
        df.replace(r"\\", '', regex=True, inplace=True)
        df.replace('years', '', regex=True, inplace=True)

        df['City'] = df['City'].map(lambda x: x.capitalize())
        df['Email'] = df['Email'].map(lambda x: x.lower())
        df['LastName'] = df['LastName'].map(lambda x: x.capitalize())
        df['FirstName'] = df['FirstName'].map(lambda x: x.capitalize())
        df['Country'] = df['Country'].map(lambda x: 'U.S.A')
        df['Age'] = df['Age'].map(lambda x: int(x[:2]))
        df['UserName'] = df['UserName'].map(lambda x: x.lower())




def my_m_and_a(conten1, content2, content3):
    filter1(conten1)
    filter2(content2)
    # filter3(content3)

my_m_and_a('only_wood_customer_us_1.csv',
           'only_wood_customer_us_2.csv',
           'only_wood_customer_us_3.csv')