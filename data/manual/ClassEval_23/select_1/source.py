class CombinationCalculator:
    def select(elements, num):
        combinations = list(itertools.combinations(elements, num))
        return combinations