class ExpressionCalculator:
    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        # Remove any whitespace from the expression
        expression = expression.replace(" ", "")
    
        # Add a space before and after each operator
        operators = ['+', '-', '*', '/', '^', '(', ')']
        for operator in operators:
            expression = expression.replace(operator, f" {operator} ")
    
        # Remove any double spaces
        expression = expression.replace("  ", " ")
    
        # Assign the prepared infix expression to the postfix_stack attribute
        self.postfix_stack = expression.split()