class BigNumCalculator:
    def subtract(self, num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'
        """
        # Convert the numbers to integers
        num1 = int(num1)
        num2 = int(num2)
        
        # Subtract the numbers
        result = num1 - num2
        
        # Return the result
        return str(result)