class SQLQueryBuilder:
    def select(table, columns, conditions):
        # Start building the SELECT SQL statement
        sql = "SELECT "
    
        # Add the columns to the SELECT statement
        sql += ", ".join(columns)
    
        # Add the table to the SELECT statement
        sql += " FROM " + table
    
        # Add the conditions to the SELECT statement
        if conditions:
            sql += " WHERE " + conditions
    
        # Return the generated SQL statement
        return sql