class TriCalculator:
    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        angle_rad = radians(x)
        tan_value = tan(angle_rad)
        return tan_value