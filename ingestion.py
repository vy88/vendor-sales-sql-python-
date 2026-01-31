import pandas as pd
import os
import time
import logging
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create database engine
engine = create_engine('sqlite:///inventory.db')

# Data folder path
data_path = r"D:\data science\vendor project\csv files"


def ingest_db(df, table_name):
    """Ingest dataframe into database table"""
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)


def load_raw_data():
    """Load CSV files and ingest into database"""
    start = time.time()

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            file_path = os.path.join(data_path, file)
            table_name = file[:-4]   # remove .csv

            df = pd.read_csv(file_path)
            ingest_db(df, table_name)

            logging.info(f"{file} loaded into table {table_name}")
if __name__ == "__main__":
    load_raw_data()
    import pandas as pd
    import os
    import time
    import logging
    from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create database engine
engine = create_engine('sqlite:///inventory.db')

# Data folder path
data_path = r"D:\data science\vendor project\csv files"


def ingest_db(df, table_name):
    """Ingest dataframe into database table"""
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)


def load_raw_data():
    """Load CSV files and ingest into database"""
    start = time.time()

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            file_path = os.path.join(data_path, file)
            table_name = file[:-4]   # remove .csv

            df = pd.read_csv(file_path)
            ingest_db(df, table_name)

            logging.info(f"{file} loaded into table {table_name}")
if __name__ == "__main__":
    load_raw_data()