class SQLGenerator:
    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        """
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
            
        # Generate the complete UPDATE SQL statement
        sql_statement = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition};"
            
        return sql_statement