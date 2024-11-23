class ComplexCalculator:
    def multiply(c1, c2):
        """
        Multiplies two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The product of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.multiply(1+2j, 3+4j)
        (-5+10j)

        """
        real_part = (c1.real * c2.real) - (c1.imag * c2.imag)
        imag_part = (c1.real * c2.imag) + (c1.imag * c2.real)
        result = complex(real_part, imag_part)
        return result