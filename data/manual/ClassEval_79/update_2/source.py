class SQLGenerator:
    def update(table, data, condition):
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
        
        # Generate the WHERE clause of the SQL statement
        where_clause = ' AND '.join([f"{key} = '{value}'" for key, value in condition.items()])
        
        # Generate the complete UPDATE SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} WHERE {where_clause};"
        
        return sql_statement