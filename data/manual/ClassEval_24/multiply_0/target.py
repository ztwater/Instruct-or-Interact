class ComplexCalculator:
    def multiply(c1, c2):
        real_part = (c1.real * c2.real) - (c1.imag * c2.imag)
        imag_part = (c1.real * c2.imag) + (c1.imag * c2.real)
        result = complex(real_part, imag_part)
        return result