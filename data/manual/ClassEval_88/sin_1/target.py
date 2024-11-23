class TriCalculator:
    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        # Convert the angle from degrees to radians
        angle_in_radians = math.radians(x)
        
        # Calculate the sin value of the angle
        sin_value = math.sin(angle_in_radians)
        
        return sin_value