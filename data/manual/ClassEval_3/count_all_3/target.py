class ArrangementCalculator:
    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :param n: int, the total number of items.
        :return: int, the count of all arrangements.
        >>> ArrangementCalculator.count_all(4)
        64
        """
        total_count = 0
        for i in range(1, n+1):
            total_count += ArrangementCalculator.nCr(n, i)
        return total_count
