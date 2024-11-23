class ArrangementCalculator:
    def select_all(self):
        arrangements = []
        for i in range(1, len(self.datas) + 1):
            for arrangement in itertools.permutations(self.datas, i):
                arrangements.append(list(arrangement))
        return arrangements