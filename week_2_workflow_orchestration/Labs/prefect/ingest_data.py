# Require Libararies
import argparse
import os
import pyarrow.parquet as pq
import pandas as pd
from time import time
# Using sqlalchemy to access postgres data
from sqlalchemy import create_engine
# To automate this job
from prefect import flow, task
# Flow is a magic function, It takes input, prefrom work, and return output


# Adding task decorators
# Adding some parameters: to log prints, and retry the task when fails 
@task(log_prints=True, retries=3)
def ingest_data(user, password, host, port, db, table_name, url, data_format):
    print("Here in Task")
    # Download csv file
    data_name = f'output.{data_format}'
    csv_name = 'output.csv'

    # Define engine to connect to postgres
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    # Start the connection
    engine.connect()

    # Download data file
    os.system(f"wget {url} -O {data_name}")

    if data_format == 'parquet':
        # Read the Parquet file
        table = pq.read_table(data_name)

        # Convert to a Pandas DataFrame
        df = table.to_pandas()

        # To free storage
        del table

        # Save DataFrame as CSV
        df.to_csv(csv_name, index=False)

    # Now we need to fetch our dataset into our database
    # But the data is too big, so we will use chunks to fetch the dataset, using iterator
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df['tpep_pickup_datetime'] = pd.to_datetime(df.tpep_pickup_datetime)
    df['tpep_dropoff_datetime'] = pd.to_datetime(df.tpep_dropoff_datetime)

    # We first need to create a table, then ingest the data inside that table
    # Ingesting data chucks into sql database
    # Create a table with only table names.
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Go check in pgcli terminal:
    # - \dt will tell you what database schema we have.
    # - \d <table_name> will describe the schema, press q to quit
    # Now ingest the data into table.
    df.to_sql(name=table_name, con=engine, if_exists='append')

    # Check if the data is ingested successfully
    # - In Terminal pgcli: SELECT COUNT(*) FROM yellow_taxi_data
    # Now we want to ingest the rest of dataframe
    while True:

        t_start = time()

        df = next(df_iter, None)

        if df is not None:
            df['tpep_pickup_datetime'] = pd.to_datetime(df.tpep_pickup_datetime)
            df['tpep_dropoff_datetime'] = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=table_name, con=engine, if_exists='append')
            
            t_end = time()

            print(f'Inserted another chuck..., took {round(t_end-t_start, 3)} second')

        else: 
            print("All data has beed ingested successfully!!!")
            break


# Automation
@flow(name='Ingest Flow')
def main_flow():
    print("Here in Main FLOW func")
    # user
    # password
    # host
    # port
    # data
    # database name
    # table name
    # url of the csv
    # Extract parameters
    user = 'root'
    password = 'root'
    host = 'pgdatabase'
    port = '5432'
    db = 'ny_taxi'
    table_name = 'yellow_taxi_data'
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"  
    data_format = 'parquet'

    ingest_data(user, password, host, port, db, table_name, url, data_format)

if __name__ == '__main__':
    print("Here in Main")
    # Call main to excute target code.
    main_flow()