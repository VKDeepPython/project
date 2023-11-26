from database_creator import DatabaseCreator
from connection import Connection
from model import Model

if __name__ == '__main__':
    creator = DatabaseCreator()
    creator.create_database()

    conn = Connection()
    table_name = "Users"
    columns = {"name": str, "age": int}
    users = Model(conn, table_name, columns)
    print(users.insert(["name", "age"], ["test", 21]))
    print(users.insert(["name", "age"], ["some person", 45]))
    print(users.all())
    print(users.find("name", "test"))
    print(users.delete("name", "test"))
    print(users.all())
    new_values = {"age": 50}
    print(users.update(new_values, "name", "some person"))
    print(users.all())
    
    orders = Model(conn, "Orders", {"name": str, "is available": bool})
    print(orders.insert(["name", "is available"], ["test", False]))
    print(orders.all())