class TriCalculator:
    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        """
        angle_in_radians = radians(x)
        sin_value = sin(angle_in_radians)
        
        return sin_value
