class SQLQueryBuilder:
    def update(table, data, where=None):
        set_clause = ', '.join([f"{column} = '{value}'" for column, value in data.items()])
        where_clause = f"WHERE {', '.join([f"{k} = '{v}'" for k, v in where.items()])}" if where else ''
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"
        return sql_statement