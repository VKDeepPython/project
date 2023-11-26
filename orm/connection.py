import psycopg2
from orm.config import Config

class Connection:
    def __init__(self, config_path='config.yaml'):
        self.config = Config(config_path)
        self.conn = None
        self.cur = None
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.config['created_dbname'],
                user=self.config['created_user'],
                host=self.config['created_host'],
                password=self.config['created_password'],
                port=self.config['created_port']
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
