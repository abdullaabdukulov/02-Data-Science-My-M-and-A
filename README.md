# Welcome to My M And A
***

### Task

The challenge revolves around merging three distinct customer databases (content_database_1, content_database_2, and content_database_3) with varying structures and inconsistencies.

Key obstacles include: 1. Diverse Data Structures: Each database differs in format, demanding alignment and standardization. 2. Data Standardization: Inconsistencies in gender representation, column order, and delimiters require harmonization. 3. Data Integrity: Ensuring a unified dataset free from duplications or discrepancies for accurate analysis.

The goal is to leverage the my_m_and_a Python function to process, clean, and merge these databases into a cohesive and standardized dataset suitable for analysis and integration into the Plastic Free Boutique project.

### Description

This Python function, my_m_and_a, is designed to merge three customer databases into a unified dataset for analysis and usage within the Plastic Free Boutique project.
### How the function works:

The function processes each database file (content_database_1, content_database_2, and content_database_3) following these steps:


1. **`content_database_1`:**
   - Reads the CSV file into a DataFrame.
   - Drops the "UserName" column.
   - Converts gender values to standardize them as "Male" or "Female".

2. **`content_database_2`:**
   - Reads the CSV file with a delimiter of ';' and no header.
   - Splits column 3 into "FirstName" and "LastName".
   - Reorders columns to match the schema: 'Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City'.
   - Standardizes gender values as "Male" or "Female".

3. **`content_database_3`:**
   - Reads the CSV file using '\\' as the delimiter and no header.
   - Extracts columns for 'Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country'.
   - Cleans and formats data by removing unnecessary characters and converting data types.
The function then merges the three processed DataFrames into a single DataFrame, performing additional data cleaning, such as capitalizing city names and ensuring consistent data types. The resulting merged DataFrame contains a consolidated set of customer data ready for further analysis or integration into the Plastic Free Boutique project.
### Installation
    1. Clone the project from the Git repository.
    2. Ensure you have Python installed.
    3. Place the following files in your project directory:
        - `my_ds_babel.py`
        - `all_fault_line.db`
        - `list_fault_line.csv`
        - `list_volcano.csv`
        - `only_wood_customer_us_1.csv`
        - `only_wood_customer_us_2.csv`
        - `only_wood_customer_us_3.csv`
    No need to install dependencies like Pandas or Io.



### Usage
To execute the project, use the following command:
Make sure to replace `content_database_1.csv`, `content_database_2.csv`, and `content_database_3.csv` with the respective paths to the CSV files containing customer data to merge.
