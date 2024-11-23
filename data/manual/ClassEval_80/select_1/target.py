class SQLQueryBuilder:
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
        # Start building the SELECT SQL statement
        sql = "SELECT "
    
        # Add the columns to the SELECT statement
        sql += ", ".join(columns)
    
        # Add the table to the SELECT statement
        sql += " FROM " + table
    
        # Add the conditions to the SELECT statement
        if where:
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key}='{value}'")
            sql += " WHERE " + " AND ".join(conditions)
    
        # Return the generated SQL statement
        return sql