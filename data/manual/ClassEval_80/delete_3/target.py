class SQLQueryBuilder:
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be executed with DELETE operation in the database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
        condition = ""
        if where:
            condition = " AND ".join("{}='{}'".format(k, v) for k, v in where.items())
        sql_statement = "DELETE FROM {} WHERE {}".format(table, condition)
        return sql_statement