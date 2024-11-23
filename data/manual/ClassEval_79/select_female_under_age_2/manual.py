### Method Description:
    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        >>> sql.select_female_under_age(30)
        "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """

### Solution Code:
    def select_female_under_age(self, age):
        condition = f"age < {age} AND gender = 'female'"
        return self.select(condition=condition)

### Source Code:
    def select_female_under_age(age):
        sql_statement = "SELECT * FROM table_name WHERE gender = 'female' AND age < {}".format(age)
        return sql_statement

### Predicted Code:
    def select_female_under_age(self, age):
        sql_statement = "SELECT * FROM {} WHERE age < {} AND gender = 'female';".format(self.table_name, age)
        return sql_statement

### Adaptation:
Total number: 5
### Raw Output:
```python
def select_female_under_age(self, age):
    sql_statement = "SELECT * FROM {} WHERE age < {} AND gender = 'female';".format(self.table_name, age)
    return sql_statement
```

### Test Code:
class SQLGeneratorTestSelectFemaleUnderAge(unittest.TestCase):
    def test_select_female_under_age(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(30)
        self.assertEqual(result, "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';")

    def test_select_female_under_age_2(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(40)
        self.assertEqual(result,"SELECT * FROM table1 WHERE age < 40 AND gender = 'female';")

    def test_select_female_under_age_3(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(20)
        self.assertEqual(result,"SELECT * FROM table1 WHERE age < 20 AND gender = 'female';")

    def test_select_female_under_age_4(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(10)
        self.assertEqual(result,"SELECT * FROM table1 WHERE age < 10 AND gender = 'female';")

    def test_select_female_under_age_5(self):
        sql = SQLGenerator('table1')
        result = sql.select_female_under_age(50)
        self.assertEqual(result,"SELECT * FROM table1 WHERE age < 50 AND gender = 'female';")

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: select


