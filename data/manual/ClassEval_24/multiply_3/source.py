class ComplexCalculator:
    def multiply(a, b):
        real_part = (a.real * b.real) - (a.imag * b.imag)
        imag_part = (a.real * b.imag) + (a.imag * b.real)
        result = complex(real_part, imag_part)
        return result