import psycopg2
from config import config

class Connection:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=config['dbname'],
                user=config['user'],
                host=config['host'],
                password=config['password'],
                port=config['port']
            )
            self.cur = self.conn.cursor()
            print("Connected to the database.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def execute(self, query, params=None):
        try:
            # print("SQL: ", query)
            self.cur.execute(query, params)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch(self, query, params=None):
        # print("SQL: ", query)
        self.cur.execute(query, params)
        return self.cur.fetchall()

    def close(self):
        self.conn.close() 

    def __del__(self):
        self.close()


if __name__ == '__main__':
    connection = Connection()
