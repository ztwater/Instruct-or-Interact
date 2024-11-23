class ArrangementCalculator:
    def select_all(internal_datas):
        arrangements = []
        for i in range(1, len(internal_datas) + 1):
            for j in range(len(internal_datas) - i + 1):
                arrangement = internal_datas[j:j+i]
                arrangements.append(arrangement)
        return arrangements