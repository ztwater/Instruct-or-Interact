class CombinationCalculator:
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :param n: The total number of elements, int.
        :return: The number of all possible combinations, int. If the number of combinations is greater than 2^63-1, return float("inf").
        """
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            count = 0
            for i in range(1, n+1):
                count += CombinationCalculator.count_all(n-i)
            if count > math.pow(2, 63) - 1:
                return float("inf")
            else:
                return count