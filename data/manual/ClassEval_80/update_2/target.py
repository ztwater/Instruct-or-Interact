class SQLQueryBuilder:
    def update(table, data, where=None):
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{column} = '{value}'" for column, value in data.items()])
        
        # Generate the WHERE clause of the SQL statement
        where_clause = ''
        if where:
            where_clause = 'WHERE ' + ' AND '.join([f"{column} = '{value}'" for column, value in where.items()])
        
        # Combine the clauses to form the complete SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"
        
        return sql_statement