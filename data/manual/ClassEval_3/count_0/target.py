class ArrangementCalculator:
    def count(n, m=None):
        """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :param n: int, the total number of items.
        :param m: int, the number of items to be chosen (default=None).
        :return: int, the count of arrangements.
        >>> ArrangementCalculator.count(5, 3)
        60
        """
        import math
        if m is None or n == m:
            return ArrangementCalculator.factorial(n)
        return math.perm(n, m)