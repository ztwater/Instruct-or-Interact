class SQLGenerator:
    def select_by_age_range(min_age, max_age):
        sql_statement = "SELECT * FROM records WHERE age >= {} AND age <= {};".format(min_age, max_age)
        return sql_statement