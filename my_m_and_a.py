from utils import (
    load_dataset_1,
    load_dataset_2,
    load_dataset_3)
from utils import (
    clean_dataset_1,
    clean_dataset_2,
    clean_dataset_3
)
import my_ds_babel
from utils import whole_dataset
from io import StringIO

csv_1 = "customer_1.csv"
csv_2 = "customer_2.csv"
csv_3 = "customer_3.csv"


def my_m_and_a(content_database_1, content_database_2, content_database_3):
    # csv1 = StringIO(content_database_1)
    # csv2 = StringIO(content_database_2)
    # csv3 = StringIO(content_database_3)
    df_1 = load_dataset_1(content_database_1)
    d1 = clean_dataset_1(df_1)
    df_2 = load_dataset_2(content_database_2)
    d2 = clean_dataset_2(df_2)
    df_3 = load_dataset_3(content_database_3)
    d3 = clean_dataset_3(df_3)
    return whole_dataset(d1, d2, d3)


merged_csv = my_m_and_a(csv_1, csv_2, csv_3)
my_ds_babel.csv_to_sql(merged_csv, db_name='ready.db', table_name='customers')
