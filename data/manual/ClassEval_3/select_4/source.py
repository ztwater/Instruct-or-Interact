class ArrangementCalculator:
    def select(datas, m):
        arrangements = []
        select_items(datas, m, [], arrangements)
        return arrangements
    