class ExpressionCalculator:
    def transform(infix_expression):
        transformed_expression = ""
        stack = []
    
        # Define the precedence of operators
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
        for char in infix_expression:
            # If the character is an operand, append it to the transformed expression
            if char.isalnum():
                transformed_expression += char
            # If the character is an opening parenthesis, push it to the stack
            elif char == '(':
                stack.append(char)
            # If the character is a closing parenthesis, pop operators from the stack and append them to the transformed expression until an opening parenthesis is encountered
            elif char == ')':
                while stack and stack[-1] != '(':
                    transformed_expression += stack.pop()
                stack.pop()  # Remove the opening parenthesis from the stack
            # If the character is an operator, pop operators from the stack and append them to the transformed expression until an operator with lower precedence or an opening parenthesis is encountered
            elif char in precedence:
                while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                    transformed_expression += stack.pop()
                stack.append(char)
    
        # Pop any remaining operators from the stack and append them to the transformed expression
        while stack:
            transformed_expression += stack.pop()
    
        return transformed_expression