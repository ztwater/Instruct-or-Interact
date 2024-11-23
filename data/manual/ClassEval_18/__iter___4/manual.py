### Method Description:
    def __iter__(self):
        """
        Returning Iterateable Objects with Own Data
        :return:Iterator
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__iter__()
        <dict_keyiterator object at 0x0000026739977C20>
        """

### Solution Code:
    def __iter__(self):
        return iter(self._data)

### Source Code:
    def __iter__(self):
        return iter(self.data)


### Predicted Code:
    def __iter__(self):
        """
        Returning Iterateable Objects with Own Data
        :return:Iterator
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__iter__()
        <dict_keyiterator object at 0x0000026739977C20>
        """
        return iter(self._data.keys())

### Adaptation:
Total number: 6
### Raw Output:
```
    def __iter__(self):
        """
        Returning Iterateable Objects with Own Data
        :return:Iterator
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__iter__()
        <dict_keyiterator object at 0x0000026739977C20>
        """
        return iter(self._data.keys())
```

### Test Code:
class CamelCaseMapTestIter(unittest.TestCase):
    def test_iter_1(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_name'] = 'John'
        camelize_map['last_name'] = 'Doe'
        camelize_map['age'] = 30
        lst = ['firstName', 'lastName', 'age']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

    def test_iter_2(self):
        camelize_map = CamelCaseMap()
        camelize_map['firstname'] = 'John'
        camelize_map['lastname'] = 'Doe'
        camelize_map['age'] = 30
        lst = ['firstname', 'lastname', 'age']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

    def test_iter_3(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_Name'] = 'John'
        camelize_map['last_Name'] = 'Doe'
        camelize_map['age'] = 30
        lst = ['firstName', 'lastName', 'age']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

    def test_iter_4(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_Name'] = 'John'
        camelize_map['last_Name'] = 'Doe'
        lst = ['firstName', 'lastName']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

    def test_iter_5(self):
        camelize_map = CamelCaseMap()
        camelize_map['first_Name'] = 'John'
        lst = ['firstName']
        iter = camelize_map.__iter__()
        i = 0
        for key in iter:
            self.assertEqual(key, lst[i])
            i += 1

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self._data
# method_dependencies: 


