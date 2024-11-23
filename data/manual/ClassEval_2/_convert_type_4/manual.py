### Method Description:
    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value oherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        """

### Solution Code:
    def _convert_type(self, arg, value):
        try:
            return self.types[arg](value)
        except (ValueError, KeyError):
            return value

### Source Code:
    def _convert_type(self, value):
        for t in self.types:
            try:
                converted_value = t(value)
                return converted_value
            except ValueError:
                pass
        return value

### Predicted Code:
    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value oherwise
        """
        for key, arg_type in self.types.items():
            if key == arg:
                try:
                    converted_value = arg_type(value)
                    return converted_value
                except ValueError:
                    pass
        return value

### Adaptation:
Total number: 10
### Raw Output:
```
def _convert_type(self, arg, value):
    """
    Try to convert the type of input value by searching in self.types.
    :param value: str, the input value in command line
    :return: return corresponding value in self.types if convert successfully, or the input value oherwise
    """
    for key, arg_type in self.types.items():
        if key == arg:
            try:
                converted_value = arg_type(value)
                return converted_value
            except ValueError:
                pass
    return value
```

### Test Code:
class ArgumentParserTestConvertType(unittest.TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test_convert_type_1(self):
        self.parser.types = {"age": int}
        result = self.parser._convert_type("age", "25")
        self.assertEqual(result, 25)

    # fail
    def test_convert_type_2(self):
        self.parser.types = {"age": int}
        result = self.parser._convert_type("age", "twenty-five")
        self.assertEqual(result, "twenty-five")

    def test_convert_type_3(self):
        self.parser.types = {"age": int}
        result = self.parser._convert_type("age", "25")
        self.assertEqual(result, 25)

    def test_convert_type_4(self):
        self.parser.types = {"age": int, "verbose": bool}
        result = self.parser._convert_type("verbose", "True")
        self.assertEqual(result, True)
    
    def test_convert_type_5(self):
        self.parser.types = {"age": int, "verbose": bool}
        result = self.parser._convert_type("verbose", "False")
        self.assertEqual(result, True)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.types
# method_dependencies: 


