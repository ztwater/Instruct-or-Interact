class BigNumCalculator:
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply, str.
        :param num2: The second number to multiply, str.
        :return: The product of the two numbers, str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'
        """
        return str(int(num1) * int(num2))