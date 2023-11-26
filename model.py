from connection import Connection

class Model:
    def __init__(self, connection, table_name, columns):
        self.conn = connection
        self.table_name = table_name
        self.columns = columns

        # Создаем таблицу, если ее нет
        self.create_table()

    def create_table(self):
        # Соответствие типов данных Python и PostgreSQL
        type_mapping = {
            int: 'INTEGER',
            str: 'VARCHAR(255)',
            float: 'REAL',
            bool: 'BOOLEAN',
        }
        
        columns_definition = ["id SERIAL PRIMARY KEY"]
        for column_name, column_type in self.columns.items():
            pg_type = type_mapping.get(column_type, 'VARCHAR(255)')
            columns_definition.append(f'{column_name} {pg_type}')
        
        query = f"CREATE TABLE IF NOT EXISTS \"{self.table_name}\" ({', '.join(columns_definition)});"
        self.conn.execute(query)

    def all(self):
        query = f"SELECT * FROM \"{self.table_name}\""
        return self.conn.fetch(query)
    
    def find(self, column, value):
        if isinstance(value, str):
            sql_value = '\'' + value + '\''
        elif isinstance(value, int) or isinstance(value, float):
            sql_value = str(value)
        elif isinstance(value, bool):
            sql_value = str(value).upper()
        query = f"SELECT * FROM \"{self.table_name}\" WHERE {column} = {sql_value}"
        return self.conn.fetch(query)
    
    def insert(self, columns, values):
        sql_columns = ', '.join(columns)
        sql_values = ''
        for value in values:
            if isinstance(value, str):
                sql_values += '\'' + value + '\''
            elif isinstance(value, int) or isinstance(value, float):
                sql_values += str(value)
            elif isinstance(value, bool):
                sql_values += str(value).upper()
            sql_values += ','
        sql_values = sql_values[:-1]
        query = f"INSERt INTO \"{self.table_name}\" ({sql_columns}) VALUES ({sql_values}) RETURNING id;"
        return self.conn.fetch(query)


if __name__ == '__main__':
    conn = Connection()
    table_name = "Users"
    columns = {"name": str, "age": int}
    user = Model(conn, table_name, columns)
    print(user.insert(["name", "age"], ["test", 21]))
    print(user.insert(["name", "age"], ["some person", 45]))
    print(user.all())
    print(user.find("name", "test"))
