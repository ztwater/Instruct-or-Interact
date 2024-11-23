class TriCalculator:
    def taylor(x, n):
        x_rad = x / 180 * math.pi
        result = 0
    
        for i in range(n+1):
            term = ((-1) ** i) * (x_rad ** (2 * i)) / math.factorial(2 * i)
            result += term
    
        return result