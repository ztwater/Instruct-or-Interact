class SQLGenerator:
    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        """
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        sql_statement = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values});"
        return sql_statement
