class SQLQueryBuilder:
    def update(table, values, condition):
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{column} = '{value}'" for column, value in values.items()])
        
        # Generate the WHERE clause of the SQL statement
        where_clause = f"WHERE {condition}"
        
        # Combine the clauses to form the complete SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"
        
        return sql_statement