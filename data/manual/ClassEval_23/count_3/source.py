class CombinationCalculator:
    def count(n, r):
        # Calculate the factorial of n
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n-1)
        
        # Calculate the number of combinations using the factorial formula
        combinations = factorial(n) // (factorial(r) * factorial(n-r))
        
        return combinations