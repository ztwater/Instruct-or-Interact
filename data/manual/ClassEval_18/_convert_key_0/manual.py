### Method Description:
    def _convert_key(self, key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._convert_key('first_name')
        'firstName'
        """

### Solution Code:
    def _convert_key(self, key):
        if isinstance(key, str):
            return self._to_camel_case(key)
        return key

### Source Code:
    def _convert_key(key):
        words = key.split('_')
        camel_case = words[0] + ''.join(word.title() for word in words[1:])
        return camel_case

### Predicted Code:
    def _convert_key(self, key):
        words = key.split('_')
        camel_case = words[0] + ''.join(word.title() for word in words[1:])
        return camel_case

### Adaptation:
Total number: 1
### Raw Output:
To adapt the `_convert_key` method to the class context of `CamelCaseMap`, you can include it as a member method within the class definition. Here's the adapted method:

```
    def _convert_key(self, key):
        words = key.split('_')
        camel_case = words[0] + ''.join(word.title() for word in words[1:])
        return camel_case
```

Note that the `self` parameter is added as the first parameter to the method, which allows the method to access the instance variables of the class. This is necessary since the method is now a member method of the `CamelCaseMap` class.

### Test Code:
class CamelCaseMapTestConvertKey(unittest.TestCase):
    def test_convert_key_1(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('aaa_bbb'), 'aaaBbb')

    def test_convert_key_2(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('first_name'), 'firstName')

    def test_convert_key_3(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('last_name'), 'lastName')

    def test_convert_key_4(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('ccc_ddd'), 'cccDdd')

    def test_convert_key_5(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key('eee_fff'), 'eeeFff')

    def test_convert_key_6(self):
        camelize_map = CamelCaseMap()
        self.assertEqual(camelize_map._convert_key(1234), 1234)

### Test Output:
# 1 errors, 0 failures in 6 runs.
# errors:
#     AttributeError:
#         test_convert_key_6: 'int' object has no attribute 'split'
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: _to_camel_case


