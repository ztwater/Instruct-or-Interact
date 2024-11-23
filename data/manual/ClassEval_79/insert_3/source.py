class SQLGenerator:
    def insert(table_name, data):
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        return sql_statement