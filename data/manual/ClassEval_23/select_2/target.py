class CombinationCalculator:
    def select(self, m: int) -> List[List[str]]:
        combinations = list(itertools.combinations(self.datas, m))
        return combinations
