class ExpressionCalculator:
    def prepare(infix_expression):
        # Remove any whitespace from the expression
        infix_expression = infix_expression.replace(" ", "")
    
        # Add a space before and after each operator
        operators = ['+', '-', '*', '/', '^', '(', ')']
        for operator in operators:
            infix_expression = infix_expression.replace(operator, f" {operator} ")
    
        # Remove any double spaces
        infix_expression = infix_expression.replace("  ", " ")
    
        # Return the prepared infix expression
        return infix_expression