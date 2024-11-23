class SQLQueryBuilder:
    def update(table, data, where=None):
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{column}='{value}'" for column, value in data.items()])

        # Generate the WHERE clause of the SQL statement
        # Combine the conditions with AND operator if there are multiple conditions
        if where:
            where_clause = ' AND '.join([f"{column}='{value}'" for column, value in where.items()])
            where_clause = f"WHERE {where_clause}"
        else:
            where_clause = ""

        # Combine the clauses to form the complete SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"

        return sql_statement