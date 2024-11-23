### Method Description:
    @staticmethod
    def _to_camel_case(key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """

### Solution Code:
    @staticmethod
    def _to_camel_case(key):
        parts = key.split('_')
        return parts[0] + ''.join(part.title() for part in parts[1:])

### Source Code:
    def _to_camel_case(key):
        words = key.split('_')
        camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        return camel_case

### Predicted Code:
    def _to_camel_case(self):
        """
        convert key string into camel case
        :param self: reference to the instance of CamelCaseMap
        :return: str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
        words = self.split('_')
        camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        return camel_case


### Adaptation:
Total number: 5
### Raw Output:
To adapt the `_to_camel_case` method to the class context of `CamelCaseMap`, you can modify the method as a static method of the `CamelCaseMap` class and replace `key` with `self` as the parameter. Here's the adapted method:

```
class CamelCaseMap:
    ...

    @staticmethod
    def _to_camel_case(self):
        """
        convert key string into camel case
        :param self: reference to the instance of CamelCaseMap
        :return: str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
        words = self.split('_')
        camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        return camel_case

    ...
```

Now, the `_to_camel_case` method can be accessed as a static method of the `CamelCaseMap` instances.

### Test Code:
class CamelCaseMapTestToCamelCase(unittest.TestCase):
    def test_to_camel_case_1(self):
        self.assertEqual(CamelCaseMap._to_camel_case('aaa_bbb'), 'aaaBbb')

    def test_to_camel_case_2(self):
        self.assertEqual(CamelCaseMap._to_camel_case('first_name'), 'firstName')

    def test_to_camel_case_3(self):
        self.assertEqual(CamelCaseMap._to_camel_case('last_name'), 'lastName')

    def test_to_camel_case_4(self):
        self.assertEqual(CamelCaseMap._to_camel_case('ccc_ddd'), 'cccDdd')

    def test_to_camel_case_5(self):
        self.assertEqual(CamelCaseMap._to_camel_case('eee_fff'), 'eeeFff')

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


