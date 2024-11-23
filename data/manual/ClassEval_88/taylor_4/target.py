class TriCalculator:
    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """

        x_rad = x / 180 * pi
        result = 0
    
        for i in range(n+1):
            term = ((-1) ** i) * (x_rad ** (2 * i)) / self.factorial(2 * i)
            result += term
    
        return result
