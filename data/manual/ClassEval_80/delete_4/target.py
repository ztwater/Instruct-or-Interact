class SQLQueryBuilder:
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be executed with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        """
        if where is None:
            sql_statement = "DELETE FROM {}".format(table)
        else:
            condition = " AND ".join(["{}='{}'".format(key, value) for key, value in where.items()])
            sql_statement = "DELETE FROM {} WHERE {}".format(table, condition)
        return sql_statement