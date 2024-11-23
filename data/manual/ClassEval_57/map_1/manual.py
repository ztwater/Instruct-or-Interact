### Method Description:
    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """

### Solution Code:
    @staticmethod
    def map(data):
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

                right_ranking_list = []
                count = 1
                for t in sub_list:
                    if t == 0:
                        right_ranking_list.append(0)
                    else:
                        right_ranking_list.append(count)
                        count += 1

                ap = np.sum(np.array(right_ranking_list) * ranking_array) / total_num
                return ap, [ap]

        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)

                if total_num == 0:
                    ap = 0.0
                else:
                    ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)

                    right_ranking_list = []
                    count = 1
                    for t in sub_list:
                        if t == 0:
                            right_ranking_list.append(0)
                        else:
                            right_ranking_list.append(count)
                            count += 1

                    ap = np.sum(np.array(right_ranking_list) * ranking_array) / total_num

                separate_result.append(ap)
            return np.mean(separate_result), separate_result

### Source Code:
    def map(input_data):
        # Compute the Average Precision (AP) for each data point
        ap_list = []
        for data_point in input_data:
            # Compute the precision and recall for the data point
            precision = compute_precision(data_point)
            recall = compute_recall(data_point)
            
            # Compute the Average Precision (AP) for the data point
            ap = precision * recall
            
            # Add the AP to the list of APs
            ap_list.append(ap)
        
        # Compute the Mean Average Precision (MAP) by taking the mean of APs
        map_score = sum(ap_list) / len(ap_list)
        
        return map_score

### Predicted Code:
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        def compute_precision(data_point):
            # Compute the precision for the data point
            correct_answers = sum(data_point[0])
            total_answers = len(data_point[0])
            precision = correct_answers / total_answers
            return precision
        
        def compute_recall(data_point):
            # Compute the recall for the data point
            correct_answers = sum(data_point[0])
            total_ground_truth = data_point[1]
            recall = correct_answers / total_ground_truth
            return recall
        
        if isinstance(data, tuple):
            # Compute the precision and recall for the data point
            precision = compute_precision(data)
            recall = compute_recall(data)
            
            # Compute the Average Precision (AP) for the data point
            ap = precision * recall
            
            return ap
        
        elif isinstance(data, list):
            ap_list = []
            precision_list = []
            
            for data_point in data:
                # Compute the precision and recall for the data point
                precision = compute_precision(data_point)
                recall = compute_recall(data_point)
                
                # Compute the Average Precision (AP) for the data point
                ap = precision * recall
                
                # Add the AP to the list of APs
                ap_list.append(ap)
                precision_list.append(precision)
            
            # Compute the Mean Average Precision (MAP) by taking the mean of APs
            map_score = sum(ap_list) / len(ap_list)
            
            return map_score, precision_list

### Adaptation:
Total number: 12
### Raw Output:
```python
import numpy as np
class MetricsCalculator2:  
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        def compute_precision(data_point):
            # Compute the precision for the data point
            correct_answers = sum(data_point[0])
            total_answers = len(data_point[0])
            precision = correct_answers / total_answers
            return precision
        
        def compute_recall(data_point):
            # Compute the recall for the data point
            correct_answers = sum(data_point[0])
            total_ground_truth = data_point[1]
            recall = correct_answers / total_ground_truth
            return recall
        
        if isinstance(data, tuple):
            # Compute the precision and recall for the data point
            precision = compute_precision(data)
            recall = compute_recall(data)
            
            # Compute the Average Precision (AP) for the data point
            ap = precision * recall
            
            return ap
        
        elif isinstance(data, list):
            ap_list = []
            precision_list = []
            
            for data_point in data:
                # Compute the precision and recall for the data point
                precision = compute_precision(data_point)
                recall = compute_recall(data_point)
                
                # Compute the Average Precision (AP) for the data point
                ap = precision * recall
                
                # Add the AP to the list of APs
                ap_list.append(ap)
                precision_list.append(precision)
            
            # Compute the Mean Average Precision (MAP) by taking the mean of APs
            map_score = sum(ap_list) / len(ap_list)
            
            return map_score, precision_list
```


### Test Code:
class MetricsCalculator2TestMap(unittest.TestCase):
    def test_map_1(self):
        res1, res2 = MetricsCalculator2.map(([1, 0, 1, 0], 4))
        self.assertEqual(res1, 0.41666666666666663)
        self.assertEqual(res2, [0.41666666666666663])

    def test_map_2(self):
        res1, res2 = MetricsCalculator2.map(([0, 0, 0, 1], 4))
        self.assertEqual(res1, 0.0625)
        self.assertEqual(res2, [0.0625])

    def test_map_3(self):
        res1, res2 = MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        self.assertEqual(res1, 0.3333333333333333)
        self.assertEqual(res2, [0.41666666666666663, 0.25])

    def test_map_4(self):
        res1, res2 = MetricsCalculator2.map([([1, 1, 1, 0], 4), ([0, 0, 0, 1], 4)])
        self.assertEqual(res1, 0.40625)
        self.assertEqual(res2, [0.75, 0.0625])

    def test_map_5(self):
        res1, res2 = MetricsCalculator2.map([([1, 0, 1, 1], 4), ([0, 1, 0, 0], 4)])
        self.assertEqual(res1, 0.3645833333333333)
        self.assertEqual(res2, [0.6041666666666666, 0.125])

    def test_map_6(self):
        try:
            MetricsCalculator2.map(1)
        except:
            pass

    def test_map_7(self):
        res1, res2 = MetricsCalculator2.map([])
        self.assertEqual(res1, 0.0)
        self.assertEqual(res2, [0.0])

    def test_map_8(self):
        res1, res2 = MetricsCalculator2.map([([1, 0, 1, 1], 0), ([0, 1, 0, 0], 0)])
        self.assertEqual(res1, 0.0)
        self.assertEqual(res2, [0.0, 0.0])

### Test Output:
# 4 errors, 3 failures in 8 runs.
# errors:
#     TypeError:
#         test_map_1: cannot unpack non-iterable float object
#         test_map_2: cannot unpack non-iterable float object
#     ZeroDivisionError:
#         test_map_7: division by zero
#         test_map_8: division by zero
# failures:
#     AssertionError:
#         test_map_3: 0.25 != 0.3333333333333333
#         test_map_4: 0.3125 != 0.40625
#         test_map_5: 0.3125 != 0.3645833333333333


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


