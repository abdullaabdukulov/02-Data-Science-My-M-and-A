# Task

In this project we are given three different csv files. 
We need to generalize them to sql.

# Description

First of all, since the csv files given to us are different, we will write a script to read them and process the data. 
Then we combine them into one object. 
We discard columns that are useless to us.

# Installation

We need the pandas and re libraries for data processing. 
To convert from CSV to SQL, we will use the my_ds_babel that we prepared in the previous task.

# Usage

Our my_m_and_a function is given three csv files, and it returns a summarized csv to you. 
We send the returned CSV to the csv_to_sql function in the my_ds_babel file along with the database and column names.