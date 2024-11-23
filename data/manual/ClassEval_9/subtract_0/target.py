class BigNumCalculator:
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract, str.
        :param num2: The second number to subtract, str.
        :return: The difference of the two numbers, str.
        """
        # Convert the numbers to integers
        num1 = int(num1)
        num2 = int(num2)
        
        # Subtract the numbers
        result = num1 - num2
        
        # Return the result
        return str(result)