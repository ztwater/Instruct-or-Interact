class SQLQueryBuilder:
    def insert(table_name, column_names, values):
        # Check if the number of column names matches the number of values
        if len(column_names) != len(values):
            return "Error: Number of column names does not match number of values"
        
        # Generate the INSERT SQL statement
        sql = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(values)})"
        
        return sql