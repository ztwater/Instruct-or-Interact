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
    def _to_camel_case(self, key):
        words = key.split('_')
        camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        return camel_case

### Adaptation:
Total number: 1
### Raw Output:
```
    def _to_camel_case(self, key):
        words = key.split('_')
        camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        return camel_case
```

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
# 5 errors, 0 failures in 5 runs.
# errors:
#     TypeError:
#         test_to_camel_case_1: _to_camel_case() missing 1 required positional argument: 'key'
#         test_to_camel_case_2: _to_camel_case() missing 1 required positional argument: 'key'
#         test_to_camel_case_3: _to_camel_case() missing 1 required positional argument: 'key'
#         test_to_camel_case_4: _to_camel_case() missing 1 required positional argument: 'key'
#         test_to_camel_case_5: _to_camel_case() missing 1 required positional argument: 'key'
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


