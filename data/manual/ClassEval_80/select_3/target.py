class SQLQueryBuilder:
    def select(table, columns='*', where=None):
        # Start building the SELECT SQL statement
        sql = "SELECT "
    
        # Add the columns to the SELECT statement
        sql += ", ".join(columns)
    
        # Add the table to the SELECT statement
        sql += " FROM " + table
    
        # Add the conditions to the SELECT statement
        if where:
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key}='{value}'")
            sql += " WHERE " + " AND ".join(conditions)
    
        # Return the generated SQL statement
        return sql