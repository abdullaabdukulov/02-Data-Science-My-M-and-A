from functions import FilterContent1, FilterContent2, FilterContent3, Merge
from my_ds_babel import csv_to_sql
def my_m_and_a(conten1, content2, content3):
    CleanedData1 = FilterContent1(conten1)
    CleanedData2 = FilterContent2(content2)
    CleanedData3 = FilterContent3(content3)

    Merge(CleanedData1, CleanedData2, CleanedData3)

    # csv_to_sql('merged.csv', 'your_database_name.db', 'table_name')

if __name__ == '__main__':
    my_m_and_a('only_wood_customer_us_1.csv',
               'only_wood_customer_us_2.csv',
               'only_wood_customer_us_3.csv')
