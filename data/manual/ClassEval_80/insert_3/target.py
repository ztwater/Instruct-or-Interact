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
        # Extract column names and values from the data dictionary
        column_names = list(data.keys())
        values = list(data.values())
        
        # Create placeholders for the values in the SQL statement
        value_placeholders = ', '.join(["'{}'".format(value) for value in values])
        
        # Generate the INSERT SQL statement
        query = "INSERT INTO {} ({}) VALUES ({})".format(table, ', '.join(column_names), value_placeholders)
        
        return query