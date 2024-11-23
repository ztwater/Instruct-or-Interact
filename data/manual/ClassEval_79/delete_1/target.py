class SQLGenerator:
    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        """
        sql_statement = "DELETE FROM " + self.table_name + " WHERE " + condition + ";"
        return sql_statement