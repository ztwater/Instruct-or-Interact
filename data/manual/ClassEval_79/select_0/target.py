class SQLGenerator:
    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        """
        # Convert the fields list into a string
        fields_str = ', '.join(fields)
        
        # Generate the SELECT SQL statement
        sql_statement = f"SELECT {fields_str} FROM {self.table_name}"
        
        # Add the WHERE clause if condition is provided
        if condition:
            sql_statement += f" WHERE {condition}"
        
        sql_statement += ";"
        
        return sql_statement