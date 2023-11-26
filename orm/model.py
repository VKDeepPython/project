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
            columns_definition.append(f'"{column_name}" {pg_type}')
        
        query = f"CREATE TABLE IF NOT EXISTS \"{self.table_name}\" ({', '.join(columns_definition)});"
        self.conn.execute(query)

    def __convert_type_python_to_sql(self, value):
        if isinstance(value, str):
            sql_value = '\'' + value + '\''
        elif isinstance(value, int) or isinstance(value, float):
            sql_value = str(value)
        elif isinstance(value, bool):
            sql_value = str(value).upper()
        return sql_value

    def all(self):
        query = f"SELECT * FROM \"{self.table_name}\""
        return self.conn.fetch(query)

    def find(self, column, value):
        sql_value = self.__convert_type_python_to_sql(value)
        query = f"SELECT * FROM \"{self.table_name}\" WHERE \"{column}\" = {sql_value}"
        return self.conn.fetch(query)

    def insert(self, columns, values):
        sql_columns = ', '.join(['"' + column + '"' for column in columns])
        sql_values = ''
        for value in values:
            sql_values += self.__convert_type_python_to_sql(value)
            sql_values += ','
        sql_values = sql_values[:-1]
        query = f"INSERT INTO \"{self.table_name}\" ({sql_columns}) VALUES ({sql_values}) RETURNING id;"
        return self.conn.fetch(query)

    def delete(self, column, value):
        sql_value = self.__convert_type_python_to_sql(value)
        query = f"DELETE FROM \"{self.table_name}\" WHERE \"{column}\" = {sql_value} RETURNING id;"
        return self.conn.fetch(query)

    def update(self, column_values: dict, cond_column: str, cond_value: any):
        updates = []
        for column_name, new_value in column_values.items():
            sql_new_value = self.__convert_type_python_to_sql(new_value)
            updates.append(f'\"{column_name}\" = {sql_new_value}')
        
        sql_cond_value = self.__convert_type_python_to_sql(cond_value)
        
        query = f"UPDATE \"{self.table_name}\" SET {', '.join(updates)} WHERE \"{cond_column}\" = {sql_cond_value};"
        return self.conn.execute(query)


# if __name__ == '__main__':
#     conn = Connection()
#     table_name = "Users"
#     columns = {"name": str, "age": int}
#     users = Model(conn, table_name, columns)
#     print(users.insert(["name", "age"], ["test", 21]))
#     print(users.insert(["name", "age"], ["some person", 45]))
#     print(users.all())
#     print(users.find("name", "test"))
#     print(users.delete("name", "test"))
#     print(users.all())
#     new_values = {"age": 50}
#     print(users.update(new_values, "name", "some person"))
#     print(users.all())
    
#     orders = Model(conn, "Orders", {"name": str, "is available": bool})
#     print(orders.insert(["name", "is available"], ["test", False]))
#     print(orders.all())

