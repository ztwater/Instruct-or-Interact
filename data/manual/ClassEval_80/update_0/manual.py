### Method Description:
    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """

### Solution Code:
    @staticmethod
    def update(table, data, where=None):
        update_str = ', '.join(f"{k}='{v}'" for k, v in data.items())
        query = f"UPDATE {table} SET {update_str}"
        if where:
            query += " WHERE " + ' AND '.join(f"{k}='{v}'" for k, v in where.items())
        return query

### Source Code:
    def update(table, values, condition):
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{column} = '{value}'" for column, value in values.items()])
        
        # Generate the WHERE clause of the SQL statement
        where_clause = f"WHERE {condition}"
        
        # Combine the clauses to form the complete SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"
        
        return sql_statement

### Predicted Code:
    def update(table, data, where=None):
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{column}='{value}'" for column, value in data.items()])

        # Generate the WHERE clause of the SQL statement
        # Combine the conditions with AND operator if there are multiple conditions
        if where:
            where_clause = ' AND '.join([f"{column}='{value}'" for column, value in where.items()])
            where_clause = f"WHERE {where_clause}"
        else:
            where_clause = ""

        # Combine the clauses to form the complete SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"

        return sql_statement

### Adaptation:
Total number: 9
### Raw Output:
Here is the adapted `update` method for the `SQLQueryBuilder` class:

```python
class SQLQueryBuilder:
    @staticmethod
    def update(table, data, where=None):
        # Generate the SET clause of the SQL statement
        set_clause = ', '.join([f"{column}='{value}'" for column, value in data.items()])

        # Generate the WHERE clause of the SQL statement
        # Combine the conditions with AND operator if there are multiple conditions
        if where:
            where_clause = ' AND '.join([f"{column}='{value}'" for column, value in where.items()])
            where_clause = f"WHERE {where_clause}"
        else:
            where_clause = ""

        # Combine the clauses to form the complete SQL statement
        sql_statement = f"UPDATE {table} SET {set_clause} {where_clause};"

        return sql_statement
```

This updated `update` method takes the `table` name, a dictionary of `data` containing the key-value pairs for the update statement, and an optional `where` parameter for the query condition. It generates the SQL statement by constructing the `SET` and `WHERE` clauses accordingly.

### Test Code:
class SQLQueryBuilderTestUpdate(unittest.TestCase):
    def test_update_1(self):
        self.assertEqual(
            SQLQueryBuilder.update('users', {'age': 35}, {'name': 'Tom'}),
            "UPDATE users SET age='35' WHERE name='Tom'"
        )

    def test_update_2(self):
        self.assertEqual(
            SQLQueryBuilder.update('students', {'age': 18}, {'name': 'Tom'}),
            "UPDATE students SET age='18' WHERE name='Tom'"
        )

    def test_update_3(self):
        self.assertEqual(
            SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'apple'}),
            "UPDATE items SET price='1.0' WHERE name='apple'"
        )

    def test_update_4(self):
        self.assertEqual(
            SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'aaa'}),
            "UPDATE items SET price='1.0' WHERE name='aaa'"
        )

    def test_update_5(self):
        self.assertEqual(
            SQLQueryBuilder.update('items', {'price': 1.0}, {'name': 'bbb'}),
            "UPDATE items SET price='1.0' WHERE name='bbb'"
        )

    def test_update_6(self):
        self.assertEqual(
            SQLQueryBuilder.update('items', {'price': 1.0}),
            "UPDATE items SET price='1.0'"
        )

### Test Output:
# 0 errors, 6 failures in 6 runs.
# errors:
# failures:
#     AssertionError:
#         test_update_1: "UPDATE users SET age='35' WHERE name='Tom';" != "UPDATE users SET age='35' WHERE name='Tom'"
#         test_update_2: "UPDATE students SET age='18' WHERE name='Tom';" != "UPDATE students SET age='18' WHERE name='Tom'"
#         test_update_3: "UPDATE items SET price='1.0' WHERE name='apple';" != "UPDATE items SET price='1.0' WHERE name='apple'"
#         test_update_4: "UPDATE items SET price='1.0' WHERE name='aaa';" != "UPDATE items SET price='1.0' WHERE name='aaa'"
#         test_update_5: "UPDATE items SET price='1.0' WHERE name='bbb';" != "UPDATE items SET price='1.0' WHERE name='bbb'"
#         test_update_6: "UPDATE items SET price='1.0' ;" != "UPDATE items SET price='1.0'"


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


