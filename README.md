# 02-Data-Science-My-M-and-A

# Task

This project addresses the integration of customer data from Only Wood Box into Plastic Free Boutique's database. The challenge involves merging and transforming data from three tables, ensuring compatibility with the existing database schema. The `my_m_and_a` script orchestrates this process, resulting in a consolidated dataset. Post-merge, the data is converted to SQL, stored in `plastic_free_boutique.sql` under the `customers` table, while adhering to confidentiality requirements.



# Description

This project includes Python scripts for merging and acquiring customer data from the acquired company (Only Wood Box) and saving it into the Plastic Free Boutique database. The project is structured as follows:

- `my_m_and_a.py`: Python script containing functions for merging and acquiring data.
- `my_ds_babel.py`: Python script with a function for converting CSV data to SQL.



# Installation
### Requirements

- Python 3.x
- pandas
- sqlite3

You can install the required dependencies using the following command:

```bash
pip install pandas
```


# Usage

To execute the merging and acquiring process, follow these steps:

1. Replace the placeholder CSV file names in `my_m_and_a.py` with the actual file paths or content.
2. Run the `my_m_and_a.py` script.

   ```bash
   python my_m_and_a.py
   ```

3. The merged data will be saved into the SQL database.

   ```bash
   python my_ds_babel.py
   ```
