class SQLGenerator:
    def select(self, fields=None, condition=None):
        # Convert the fields list into a string
        fields_str = ', '.join(fields) if fields else '*'
        
        # Generate the SELECT SQL statement
        sql_statement = f"SELECT {fields_str} FROM {self.table_name}"
        
        # Add the condition if provided
        if condition:
            sql_statement += f" WHERE {condition}"
        
        sql_statement += ";"
        
        return sql_statement