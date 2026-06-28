from utils import *

import psycopg2

def connect(db, user, password, host, port):
    host = dns_lookup(host) or host
    print(f"Attempting to connect to postgres at {host}:{port}")
    try:
        database_connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
        cursor = database_connection.cursor()
        cursor.execute('SELECT version()')
        postgres_version = cursor.fetchone()[0]

        print("Connection successful!")
        print(f"Postgres version: {postgres_version}")
        return database_connection
    except psycopg2.OperationalError as exception:
        print(f"Connection attempt failed: {exception}.")