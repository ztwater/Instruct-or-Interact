class CombinationCalculator:
    def select_all(data):
        def select(data, selected, index):
            if index == len(data):
                print(selected)
                return
            select(data, selected, index + 1)
            select(data, selected + [data[index]], index + 1)
    
        select(data, [], 0)