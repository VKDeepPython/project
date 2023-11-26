from orm.database_creator import DatabaseCreator
from orm.connection import Connection
from orm.model import Model

# creator = DatabaseCreator()
# creator.create_database()

conn = Connection()

table_name = "Users"
columns = {"name": str, "age": int}
users = Model(conn, table_name, columns)
