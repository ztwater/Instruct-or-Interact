class SQLGenerator:
    def select_female_under_age(age):
        sql_statement = "SELECT * FROM table_name WHERE gender = 'female' AND age < {}".format(age)
        return sql_statement