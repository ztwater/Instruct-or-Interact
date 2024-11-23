class ArrangementCalculator:
    def select(self, m=None):
        arrangements = []
        select_items(self.datas, m, [], arrangements)
        return arrangements