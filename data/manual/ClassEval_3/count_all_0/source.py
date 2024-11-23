class ArrangementCalculator:
    def count_all(n):
        total_count = 0
        for i in range(1, n+1):
            total_count += nCr(n, i)
        return total_count
    