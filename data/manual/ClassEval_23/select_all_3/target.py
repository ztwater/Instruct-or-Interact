class CombinationCalculator:
    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of selecting elements from the given data list, using the select method.
        :return: A list of combinations, List[List[str]].
        """
        
        def select(data, selected, index):
            if index == len(data):
                return [selected]
            return select(data, selected, index + 1) + select(data, selected + [data[index]], index + 1)
        
        return select(self.datas, [], 0)