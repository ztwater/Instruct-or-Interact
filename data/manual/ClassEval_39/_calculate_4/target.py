class ExpressionCalculator:
    def _calculate(self, first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        operand1 = Decimal(first_value)
        operand2 = Decimal(second_value)
        if current_op == '+':
            return operand1 + operand2
        elif current_op == '-':
            return operand1 - operand2
        elif current_op == '*':
            return operand1 * operand2
        elif current_op == '/':
            return operand1 / operand2
        else:
            return "Invalid operator"