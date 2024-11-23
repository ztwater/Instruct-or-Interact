class CombinationCalculator:
    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        if resultIndex == len(resultList):
            result.append(resultList.copy())
            return
    
        if dataIndex >= len(self.datas):
            return
    
        resultList[resultIndex] = self.datas[dataIndex]
        self._select(dataIndex + 1, resultList, resultIndex + 1, result)
        self._select(dataIndex + 1, resultList, resultIndex, result)
    
    