class ExpressionCalculator:
    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        # Remove any whitespace from the expression
        expression = expression.replace(" ", "")
        
        # Add a space before and after each operator
        operators = ['+', '-', '*', '/', '^', '(', ')']
        for operator in operators:
            expression = expression.replace(operator, f" {operator} ")
        
        # Remove any double spaces
        expression = expression.replace("  ", " ")
        
        # Split the prepared expression into a list of tokens
        tokens = expression.split(" ")
        
        # Assign the tokens to the postfix_stack member variable
        self.postfix_stack = deque(tokens)