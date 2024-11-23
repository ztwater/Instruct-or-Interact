class CombinationCalculator:
    def count(n: int, m: int) -> int:
        """
        Calculate the number of combinations for a specific count.
        :param n: The total number of elements, int.
        :param m: The number of elements in each combination, int.
        :return: The number of combinations, int.
        """
        # Calculate the factorial of n
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n-1)
        
        # Calculate the number of combinations using the factorial formula
        combinations = factorial(n) // (factorial(m) * factorial(n-m))
        
        return combinations