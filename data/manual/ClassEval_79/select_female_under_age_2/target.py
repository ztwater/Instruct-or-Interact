class SQLGenerator:
    def select_female_under_age(self, age):
        sql_statement = "SELECT * FROM {} WHERE age < {} AND gender = 'female';".format(self.table_name, age)
        return sql_statement