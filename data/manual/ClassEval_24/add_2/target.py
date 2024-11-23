class ComplexCalculator:
    def add(self, c1, c2):
        """
        Adds two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The sum of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)
        
        """
        result = c1 + c2
        return result