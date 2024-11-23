class Calculator:
    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack, and store the result at the top of the operand stack
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand_stack and operator_stack
        """
        operator = operator_stack.pop()
        num2 = operand_stack.pop()
        num1 = operand_stack.pop()

        result = self.operators[operator](num1, num2)

        operand_stack.append(result)

        return operand_stack, operator_stack