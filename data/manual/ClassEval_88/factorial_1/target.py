class TriCalculator:
    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        result = 1
        for i in range(1, a+1):
            result *= i
        return result
