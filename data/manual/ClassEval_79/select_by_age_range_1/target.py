class SQLGenerator:
    def select_by_age_range(self, min_age, max_age):
        sql_statement = "SELECT * FROM {} WHERE age BETWEEN {} AND {};".format(self.table_name, min_age, max_age)
        return sql_statement