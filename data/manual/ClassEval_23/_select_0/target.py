class CombinationCalculator:
    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        """
        Generate combinations with a specified number of elements by recursion.
        :param dataIndex: The index of the data to be selected, int.
        :param resultList: The list of elements in the combination, List[str].
        :param resultIndex: The index of the element in the combination, int.
        :param result: The list of combinations, List[List[str]].
        :return: None.
        """
        if resultIndex == len(resultList):
            result.append(resultList.copy())
            return
        
        for i in range(dataIndex, len(self.datas)):
            resultList[resultIndex] = self.datas[i]
            self._select(i + 1, resultList, resultIndex + 1, result)