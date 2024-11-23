### Method Description:
    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """

### Solution Code:
    def mrr(data):
        if type(data) != list and type(data) != tuple:
            raise Exception("the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

        if len(data) == 0:
            return 0.0, [0.0]
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)
                mr_np = sub_list * ranking_array

                mr = 0.0
                for team in mr_np:
                    if team > 0:
                        mr = team
                        break
                return mr, [mr]

        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)

                if total_num == 0:
                    mr = 0.0
                else:
                    ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)
                    mr_np = sub_list * ranking_array

                    mr = 0.0
                    for team in mr_np:
                        if team > 0:
                            mr = team
                            break

                separate_result.append(mr)
            return np.mean(separate_result), separate_result

### Source Code:
    def mrr(data):
        reciprocal_ranks = []
        
        for query_results in data:
            for i, result in enumerate(query_results):
                if result == 1:
                    reciprocal_ranks.append(1 / (i + 1))
                    break
        
        if len(reciprocal_ranks) == 0:
            return 0
        
        return sum(reciprocal_ranks) / len(reciprocal_ranks)

### Predicted Code:
    def mrr(data):
        reciprocal_ranks = []
        
        for query_results in data:
            for i, result in enumerate(query_results[0]):
                if result == 1:
                    reciprocal_ranks.append(1 / (i + 1))
                    break
        
        if len(reciprocal_ranks) == 0:
            return 0
        
        return sum(reciprocal_ranks) / len(reciprocal_ranks)

### Adaptation:
Total number: 2
### Raw Output:
import numpy as np

class MetricsCalculator2:  
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        reciprocal_ranks = []
        
        for query_results in data:
            for i, result in enumerate(query_results[0]):
                if result == 1:
                    reciprocal_ranks.append(1 / (i + 1))
                    break
        
        if len(reciprocal_ranks) == 0:
            return 0
        
        return sum(reciprocal_ranks) / len(reciprocal_ranks)

### Test Code:
class MetricsCalculator2TestMrr(unittest.TestCase):
    def test_mrr_1(self):
        mc2 = MetricsCalculator2()
        res1, res2 = MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        self.assertEqual(res1, 1.0)
        self.assertEqual(res2, [1.0])

    def test_mrr_2(self):
        res1, res2 = MetricsCalculator2.mrr(([0, 0, 0, 1], 4))
        self.assertEqual(res1, 0.25)
        self.assertEqual(res2, [0.25])

    def test_mrr_3(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        self.assertEqual(res1, 0.75)
        self.assertEqual(res2, [1.0, 0.5])

    def test_mrr_4(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 1, 1, 0], 4), ([0, 0, 0, 1], 4)])
        self.assertEqual(res1, 0.625)
        self.assertEqual(res2, [1.0, 0.25])

    def test_mrr_5(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 1], 4), ([0, 1, 0, 0], 4)])
        self.assertEqual(res1, 0.75)
        self.assertEqual(res2, [1.0, 0.5])

    def test_mrr_6(self):
        try:
            MetricsCalculator2.mrr(1)
        except:
            pass

    def test_mrr_7(self):
        res1, res2 = MetricsCalculator2.mrr([])
        self.assertEqual(res1, 0.0)
        self.assertEqual(res2, [0.0])

    def test_mrr_8(self):
        res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 1], 0), ([0, 1, 0, 0], 0)])
        self.assertEqual(res1, 0.0)
        self.assertEqual(res2, [0.0, 0.0])

### Test Output:
# 7 errors, 0 failures in 8 runs.
# errors:
#     TypeError:
#         test_mrr_1: 'int' object is not iterable
#         test_mrr_2: 'int' object is not iterable
#         test_mrr_3: cannot unpack non-iterable float object
#         test_mrr_4: cannot unpack non-iterable float object
#         test_mrr_5: cannot unpack non-iterable float object
#         test_mrr_7: cannot unpack non-iterable int object
#         test_mrr_8: cannot unpack non-iterable float object
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


