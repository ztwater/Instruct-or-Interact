class SQLQueryBuilder:
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{column} = '{value}'" for column, value in data.items()])

        # Generate the WHERE clause of the SQL statement
        if where:
            where_clause = "WHERE " + " AND ".join([f"{column} = '{value}'" for column, value in where.items()])
        else:
            where_clause = ""

        # Combine the clauses to form the complete SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"

        return sql_statement