class SQLQueryBuilder:
    def delete(table_name, condition):
        sql_statement = "DELETE FROM {} WHERE {}".format(table_name, condition)
        return sql_statement