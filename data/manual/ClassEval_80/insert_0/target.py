class SQLQueryBuilder:
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """
        column_names = list(data.keys())
        values = list(data.values())

        # Check if the number of column names matches the number of values
        if len(column_names) != len(values):
            return "Error: Number of column names does not match number of values"

        # Convert values to string representation
        values = [str(value) for value in values]

        # Generate the INSERT SQL statement
        sql = f"INSERT INTO {table} ({', '.join(column_names)}) VALUES ({', '.join(values)})"

        return sql