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
        # Convert the angle from degrees to radians
        radians = math.radians(x)
        
        # Calculate the cosine value
        cos_value = math.cos(radians)
        
        return cos_value