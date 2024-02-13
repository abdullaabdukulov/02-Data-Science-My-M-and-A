# My_M_And_A

## Task

The task is to take 3 csv files, clean them and combine them into one sql format

## Description

This code takes a csv file and reads it using the load_dataset function and returns a dataframe.
After loading the data my clean function cleans the contents of the csv file.
Once we have cleared our files, we will combine them into one and transfer them to a new file where the func function will be imported to convert our file to sql format.

## Installation

[Data_set_1](https://storage.googleapis.com/qwasar-public/only_wood_customer_us_1.csv)

[Data_set_2](https://storage.googleapis.com/qwasar-public/only_wood_customer_us_2.csv)

[Data_set_3](https://storage.googleapis.com/qwasar-public/only_wood_customer_us_3.csv)

Libraries required to work with this code
```
    pip install pandas
    pip install db-sqlite3
    pip install tabulate
```

## Usage
* After downloading the necessary files and libraries
```
    only_wood_customer_us_1.csv
    only_wood_customer_us_1.csv
    only_wood_customer_us_1.csv

    pip install pandas
    pip install db-sqlite3
    pip install tabulate

```
Well, let's get started. Here we first download and read the contents of the clicked csv using the `def load_dataset(path)` function.

For easy reading and introduction, I use the tabulate library in the `def pretty_print(df)` function.

After reading the file, we must correct some errors like (;, -, :, /) using the `def clean_dataset_1(df)` function.

And the simplest thing is that we need to combine all our data using the `def func()` function.

We create another file called `my_ds_babel.py` and import our merged csv file.

Import all the necessary libraries `import sqlite3`, and yes I forgot something. 

We have to import our function from our main code into a new one `from my_m_and_a import func`, and create another function that simply turns our cat file into a sql file `def to_sql(merged_df)`.

<img src='a.png'>

## Help

If you have any questions you can write to me by email

> mirabbosminavarov@gmail.com
