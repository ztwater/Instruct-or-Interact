### Method Description:
    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """

### Solution Code:
    @staticmethod
    def is_operator(c):
        return c in {'+', '-', '*', '/', '(', ')', '%'}

### Source Code:
    def is_operator(char):
        operators = {'+', '-', '*', '/', '(', ')', '%'}
        return char in operators

### Predicted Code:
    def is_operator(self, c):
        operators = {'+', '-', '*', '/', '(', ')', '%'}
        return c in operators

### Adaptation:
Total number: 3
### Raw Output:
```
def is_operator(self, c):
    operators = {'+', '-', '*', '/', '(', ')', '%'}
    return c in operators
```

### Test Code:
class ExpressionCalculatorTestIsOperator(unittest.TestCase):
    def setUp(self):
        self.expression_calculator = ExpressionCalculator()

    def test_is_operator_1(self):
        self.assertTrue(self.expression_calculator.is_operator("+"))

    def test_is_operator_2(self):
        self.assertTrue(self.expression_calculator.is_operator("-"))

    def test_is_operator_3(self):
        self.assertTrue(self.expression_calculator.is_operator("*"))

    def test_is_operator_4(self):
        self.assertTrue(self.expression_calculator.is_operator("/"))

    def test_is_operator_5(self):
        self.assertFalse(self.expression_calculator.is_operator("5"))

### Test Output:
# 5 errors, 0 failures in 5 runs.
# errors:
#     TypeError:
#         test_is_operator_1: is_operator() missing 1 required positional argument: 'c'
#         test_is_operator_2: is_operator() missing 1 required positional argument: 'c'
#         test_is_operator_3: is_operator() missing 1 required positional argument: 'c'
#         test_is_operator_4: is_operator() missing 1 required positional argument: 'c'
#         test_is_operator_5: is_operator() missing 1 required positional argument: 'c'
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


