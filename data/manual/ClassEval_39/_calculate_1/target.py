class ExpressionCalculator:
    def _calculate(self, first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        first_operand = Decimal(first_value)
        second_operand = Decimal(second_value)
        
        if current_op == '+':
            return first_operand + second_operand
        elif current_op == '-':
            return first_operand - second_operand
        elif current_op == '*':
            return first_operand * second_operand
        elif current_op == '/':
            return first_operand / second_operand
        else:
            return "Invalid operator"