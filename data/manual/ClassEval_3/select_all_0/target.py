class ArrangementCalculator:
    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        """
        arrangements = []
        for i in range(1, len(self.datas) + 1):
            for arrangement in itertools.permutations(self.datas, i):
                arrangements.append(list(arrangement))
        return arrangements