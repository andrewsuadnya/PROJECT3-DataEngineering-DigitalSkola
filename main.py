import connection
import os
import sqlparse
import pandas as pd

if __name__ == "__main__":

    # connection data source
    conf = connection.config('marketplace_prod')
    conn, engine = connection.get_conn(conf, 'DataSource')
    cursor = conn.cursor()

    # connection data source
    conf = connection.config('dwh')
    conn_dwh, engine_dwh = connection.get_conn(conf, 'DataWarehouse')
    cursor_dwh = conn_dwh.cursor()

    # get query string
    path_query = os.getcwd()+'/query/'
    query = sqlparse.format(
        open(path_query+'query.sql', 'r').read(), strip_comments=True
    ).strip()

    # get schema dwh design
    dwh_design = sqlparse.format(
        open(path_query+'dwh_design.sql', 'r').read(), strip_comments=True
    ).strip()

try:
    # get data
    print('[INFO] service ETL is running..')
    df = pd.read_sql(query, engine)

    # create shema dwh
    cursor_dwh.execute(dwh_design)
    conn_dwh.commit()

    # ingest data to dwh
    df.to_sql(
        'dim_orders',
        engine_dwh,
        schema='andrewsu_dwh',
        if_exists='append',
        index=False
        )
    print('[INFO] service ETL is success..')
except Exception as e:
    print('[INFO] service ETL is failes')
    print(str(e))
