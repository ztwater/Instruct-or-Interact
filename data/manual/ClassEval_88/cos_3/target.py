class TriCalculator:
    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x:float
        :return:float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        
        radians = x * (pi / 180)  # Convert the angle from degrees to radians
        
        cos_value = self.taylor(radians, 10)  # Calculate the cosine value using Taylor series approximation
        
        return cos_value