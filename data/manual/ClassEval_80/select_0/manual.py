### Method Description:
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """

### Solution Code:
    def select(table, columns='*', where=None):
        if columns != '*':
            columns = ', '.join(columns)
        query = f"SELECT {columns} FROM {table}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query

### Source Code:
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

### Predicted Code:
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
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
                conditions.append("{}='{}'".format(key, value))
            sql += " WHERE " + " AND ".join(conditions)
    
        # Return the generated SQL statement
        return sql

### Adaptation:
Total number: 14
### Raw Output:
```
class SQLQueryBuilder:  
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """


    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
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
                conditions.append("{}='{}'".format(key, value))
            sql += " WHERE " + " AND ".join(conditions)
    
        # Return the generated SQL statement
        return sql
```

### Test Code:
class SQLQueryBuilderTestSelect(unittest.TestCase):
    def test_select_1(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["id", "name"], {'age': 30}),
            "SELECT id, name FROM users WHERE age='30'"
        )

    def test_select_2(self):
        self.assertEqual(
            SQLQueryBuilder.select('students', ["id", "name"], {'age': 18}),
            "SELECT id, name FROM students WHERE age='18'"
        )

    def test_select_3(self):
        self.assertEqual(
            SQLQueryBuilder.select('items', ["id", "name"], {'price': 1.0}),
            "SELECT id, name FROM items WHERE price='1.0'"
        )

    def test_select_4(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["id"], {'age': 30}),
            "SELECT id FROM users WHERE age='30'"
        )

    def test_select_5(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["name"], {'age': 30}),
            "SELECT name FROM users WHERE age='30'"
        )

    def test_select_6(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', ["name"]),
            "SELECT name FROM users"
        )

    def test_select_7(self):
        self.assertEqual(
            SQLQueryBuilder.select('users', "*"),
            "SELECT * FROM users"
        )

### Test Output:
# 0 errors, 0 failures in 7 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


