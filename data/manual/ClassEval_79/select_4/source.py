class SQLGenerator:
    def select(fields, table, conditions):
        # Convert the fields list into a string
        fields_str = ', '.join(fields)
        
        # Convert the conditions list into a string
        conditions_str = ' AND '.join(conditions)
        
        # Generate the SELECT SQL statement
        sql_statement = f"SELECT {fields_str} FROM {table} WHERE {conditions_str};"
        
        return sql_statement