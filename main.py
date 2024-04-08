import connection

if __name__ == "__main__":

    # connection data source
    conf = connection.config('marketplace_prod')
    print(conf)