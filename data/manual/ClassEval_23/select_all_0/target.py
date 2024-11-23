class CombinationCalculator:
    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of selecting elements from the given data list, and it uses the select method.
        :return: A list of combinations, List[List[str]].
        """
        combinations = []
        for i in range(1, len(self.datas) + 1):
            combinations.extend(self.select(i))
        return combinations