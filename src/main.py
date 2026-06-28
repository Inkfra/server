import environment
import database
from flask import Flask

db = database.connect()

db_connection = db[0]
db_cursor = db[1]

db_cursor.execute('SELECT version()')
postgres_version = db_cursor.fetchone()[0]
print(f"Connected to Postgres version: {postgres_version}")

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return "Service is running!"

db_connection.close()

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')