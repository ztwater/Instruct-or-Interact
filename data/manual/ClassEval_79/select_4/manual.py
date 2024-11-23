### Method Description:
    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        >>> sql = SQLGenerator('table1')
        >>> sql.select(['field1', 'field2'], 'filed3 = value1')
        'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
        """

### Solution Code:
    def select(self, fields=None, condition=None):
        if fields is None:
            fields = "*"
        else:
            fields = ", ".join(fields)
        sql = f"SELECT {fields} FROM {self.table_name}"
        if condition is not None:
            sql += f" WHERE {condition}"
        return sql + ";"

### Source Code:
    def select(fields, table, conditions):
        # Convert the fields list into a string
        fields_str = ', '.join(fields)
        
        # Convert the conditions list into a string
        conditions_str = ' AND '.join(conditions)
        
        # Generate the SELECT SQL statement
        sql_statement = f"SELECT {fields_str} FROM {table} WHERE {conditions_str};"
        
        return sql_statement

### Predicted Code:
    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        """
        # Convert the fields list into a string
        fields_str = ', '.join(fields)
        
        # Generate the SELECT SQL statement
        sql_statement = f"SELECT {fields_str} FROM {self.table_name}"
        
        # Add condition if provided
        if condition:
            sql_statement += f" WHERE {condition}"
        
        sql_statement += ";"
        
        return sql_statement

### Adaptation:
Total number: 28
### Raw Output:
Here is the adapted method `select` for the `SQLGenerator` class:

```
def select(self, fields=None, condition=None):
    """
    Generates a SELECT SQL statement based on the specified fields and conditions.
    :param fields: list, optional. Default is None. The list of fields to be queried.
    :param condition: str, optional. Default is None. The condition expression for the query.
    :return: str. The generated SQL statement.
    """
    # Convert the fields list into a string
    fields_str = ', '.join(fields)
    
    # Generate the SELECT SQL statement
    sql_statement = f"SELECT {fields_str} FROM {self.table_name}"
    
    # Add condition if provided
    if condition:
        sql_statement += f" WHERE {condition}"
    
    sql_statement += ";"
    
    return sql_statement
```

This method takes in `fields` and `condition` as optional parameters. It converts the `fields` list into a string and generates the initial part of the SQL statement. If a `condition` is provided, it is added to the SQL statement. Finally, the SQL statement is ended with a semicolon and returned.

### Test Code:
class SQLGeneratorTestSelect(unittest.TestCase):
    def test_select_1(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1'], "field2 = value1")
        self.assertEqual(result, "SELECT field1 FROM table1 WHERE field2 = value1;")

    def test_select_2(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1', 'field2'], "field3 = value1")
        self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1;")

    def test_select_3(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1, field2'], "field3 = value1")
        self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1;")

    def test_select_4(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1, field2'], "field3 = value1, field4 = value2")
        self.assertEqual(result, "SELECT field1, field2 FROM table1 WHERE field3 = value1, field4 = value2;")

    def test_select_5(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1'], "field2 = value1, field3 = value2")
        self.assertEqual(result, "SELECT field1 FROM table1 WHERE field2 = value1, field3 = value2;")

    def test_select_6(self):
        sql = SQLGenerator('table1')
        result = sql.select(['field1'])
        self.assertEqual(result, "SELECT field1 FROM table1;")

### Test Output:
# 0 errors, 0 failures in 6 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.table_name
# method_dependencies: 


