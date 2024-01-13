import pandas as pd
from my_ds_babel import csv_to_sql  

def my_m_and_a(content_database_1: str, content_database_2: str, content_database_3: str) -> pd.DataFrame:
    
    df1 = pd.read_csv(content_database_1)
    df2 = pd.read_csv(content_database_2)
    df3 = pd.read_csv(content_database_3)
    
    df1.dropna(inplace = True)
    df2.dropna(inplace = True)
    df3.dropna(inplace = True)

    print(df1)
    
    merged_df = pd.concat([df1, df2, df3], ignore_index=True)
    print(merged_df)
   

    return merged_df


merged_csv = my_m_and_a('only_wood_customer_us_1.csv', 'only_wood_customer_us_2.csv', 'only_wood_customer_us_3.csv')


csv_to_sql(merged_csv, 'plastic_free_boutique.sql', 'customers')
