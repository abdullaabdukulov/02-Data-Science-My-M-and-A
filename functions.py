import pandas as pd
import csv

gender = {'0': 'Male', '1': 'Female', 'F': 'Female', 'M': 'Male'}
elems = {'"': '', r'\\': '', 'boolean_': '', 'integer_': '', 'year': '', 'character_': '', 'eger_': ''}


def Filter(df):
    df.replace(elems, regex=True, inplace=True)
    df.replace(gender, inplace=True)
    df.replace('"', '', regex=True, inplace=True)
    df.replace(r"\\", '', regex=True, inplace=True)
    df.replace('years', '', regex=True, inplace=True)


    df['City'] = df['City'].map(lambda x: x.capitalize())
    df['Email'] = df['Email'].map(lambda x: x.lower())
    df['LastName'] = df['LastName'].map(lambda x: x.capitalize())
    df['FirstName'] = df['FirstName'].map(lambda x: str(x).capitalize())
    df['Country'] = df['Country'].map(lambda x: 'U.S.A')
    df['Age'] = df['Age'].map(lambda x: str(x)[:2])
    df['UserName'] = df['FirstName'].map(lambda x: x.lower())

    return df


def FilterContent1(csv_file):

    df = pd.read_csv(csv_file)
    return Filter(df)


def FilterContent2(csv_file):
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
        return Filter(df)


def FilterContent3(csv_file):
    with open(csv_file, 'r') as csvfile:
        data = dict()

        csvreader = csv.reader(csvfile, delimiter='\t')
        for row in csvreader:
            if not data:
                splited = row[0].split(',')
                for key in splited:
                    data[key] = list()
                data['FirstName'] = data.pop('Name')
                data['LastName'] = list()
            else:
                data['Gender'].append(row[0].strip('string_'))
                data['FirstName'].append(row[1].strip('string_').split(' ')[0])
                data['LastName'].append(row[1].strip('string_').split(' ')[1])
                data['Email'].append(row[2].strip('string_'))
                data['Age'].append(row[3].strip('string_'))
                data['City'].append(row[4].strip('string_'))
                data['Country'].append(row[-1])

        df = pd.DataFrame.from_dict(data, orient='columns')
        return Filter(df)



def Merge(df1, df2, df3):

    frames = [df1, df2, df3]
    df = pd.concat(frames, ignore_index=True)
    df.to_csv('merged.csv', index=False)