import environment
import database

database.connect(db=environment.POSTGRES_DB, user=environment.POSTGRES_USER, password=environment.POSTGRES_PASSWORD, host=environment.POSTGRES_HOST, port=environment.POSTGRES_PORT)
