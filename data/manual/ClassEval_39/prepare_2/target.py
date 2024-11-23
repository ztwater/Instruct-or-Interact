class ExpressionCalculator:
    def prepare(self, expression):
        # Remove any whitespace from the expression
        infix_expression = expression.replace(" ", "")
    
        # Add a space before and after each operator
        operators = ['+', '-', '*', '/', '^', '(', ')']
        for operator in operators:
            infix_expression = infix_expression.replace(operator, f" {operator} ")
    
        # Remove any double spaces
        infix_expression = infix_expression.replace("  ", " ")
    
        # Split the prepared infix expression into a list of tokens
        infix_tokens = infix_expression.split()
    
        # Convert the infix expression to postfix notation
        operator_stack = []
        for token in infix_tokens:
            if self.is_operator(token):
                while operator_stack and self.compare(token, operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                self.postfix_stack.append(token)
    
        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())