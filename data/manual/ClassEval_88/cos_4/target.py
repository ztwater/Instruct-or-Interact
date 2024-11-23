class TriCalculator:
    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x: float
        :return: float
        """

        radians = x * pi / 180
        approx = self.taylor(radians + pi / 2, 10)

        return approx
