class CombinationCalculator:
    def count_all(n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            count = 0
            for i in range(1, n+1):
                count += count_all(n-i)
            return count