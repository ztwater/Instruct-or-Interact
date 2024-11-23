class CombinationCalculator:
    def count_all(n: int) -> int:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            count = 0
            for i in range(1, n+1):
                count += CombinationCalculator.count_all(n-i)
            if count > 2**63-1:
                return float("inf")
            else:
                return count