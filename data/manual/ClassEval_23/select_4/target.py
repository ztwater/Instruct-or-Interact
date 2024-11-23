class CombinationCalculator:
    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :param m: The number of elements in each combination, int.
        :return: A list of combinations, List[List[str]].
        """
        combinations = list(itertools.combinations(self.datas, m))
        return combinations