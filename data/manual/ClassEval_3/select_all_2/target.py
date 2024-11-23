class ArrangementCalculator:
    def select_all(self):
        arrangements = []
        for i in range(1, len(self.datas) + 1):
            for j in range(len(self.datas) - i + 1):
                arrangement = self.datas[j:j+i]
                arrangements.append(arrangement)
        return arrangements