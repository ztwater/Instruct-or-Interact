class ExpressionCalculator:
    def prepare(self, expression):
        # Remove any whitespace from the expression
        expression = expression.replace(" ", "")
    
        # Add a space before and after each operator
        operators = ['+', '-', '*', '/', '^', '(', ')']
        for operator in operators:
            expression = expression.replace(operator, f" {operator} ")
    
        # Remove any double spaces
        expression = expression.replace("  ", " ")
    
        # Split the expression into a list of tokens
        tokens = expression.split()
    
        # Iterate through the tokens and handle negative numbers
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "-":
                if i == 0 or is_operator(tokens[i - 1]) or tokens[i - 1] == "(":
                    tokens[i] = f"-{tokens[i + 1]}"
                    del tokens[i + 1]
    
        # Set the prepared infix expression as the tokens
        self.postfix_stack = tokens