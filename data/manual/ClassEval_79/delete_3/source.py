class SQLGenerator:
    def delete(table, condition):
        sql_statement = "DELETE FROM " + table + " WHERE " + condition + ";"
        return sql_statement