class CombinationCalculator:
    def _select(elements, k):
        if k == 0:
            return [[]]
        if len(elements) == 0 or len(elements) < k:
            return []
        
        result = []
        for i in range(len(elements)):
            first_element = elements[i]
            remaining_elements = elements[i+1:]
            
            for combination in _select(remaining_elements, k-1):
                result.append([first_element] + combination)
        
        return result