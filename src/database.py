from utils import *
import environment

import psycopg2

def connect(db=environment.POSTGRES_DB, user=environment.POSTGRES_USER, password=environment.POSTGRES_PASSWORD, host=environment.POSTGRES_HOST, port=environment.POSTGRES_PORT):
    host = dns_lookup(host) or host
    print(f"Attempting to connect to postgres at {host}:{port}")
    try:
        connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
        cursor = connection.cursor()

        print("Connection successful!")
        return connection, cursor
    except psycopg2.OperationalError as exception:
        print(f"Connection attempt failed: {exception}.")