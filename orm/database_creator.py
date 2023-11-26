import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random
from config import Config

class DatabaseCreator:
    def __init__(self, config_path='config.yaml') -> None:
        self.config = Config(config_path)
        self.connection = psycopg2.connect(
            dbname=self.config['default_dbname']
        )
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 

    def create_database(self):
        try:
            db_create_query = sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(self.config['created_dbname'])
                )
            
            with self.connection.cursor() as cur:
                cur.execute(db_create_query)

            user_create_query = sql.SQL("CREATE USER {username} WITH PASSWORD '{password}'").format(
                    username=sql.Identifier(self.config['created_user']),
                    password=sql.Placeholder()
                )
            
            password = random.randint(100_000, 999_999)

            with self.connection.cursor() as cur:
                cur.execute(user_create_query, (password, ))
            
            self.config['created_password'] = password
        except Exception as e:
            print(e)
