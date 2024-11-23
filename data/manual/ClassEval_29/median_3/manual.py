### Method Description:
    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """

### Solution Code:
    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            middle = n // 2
            return round((sorted_data[middle - 1] + sorted_data[middle]) / 2, 2)
        else:
            middle = n // 2
            return sorted_data[middle]

### Source Code:
    def median(data):
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            median1 = sorted_data[length // 2]
            median2 = sorted_data[length // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = sorted_data[length // 2]
        return round(median, 2)

### Predicted Code:
    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            median1 = sorted_data[length // 2]
            median2 = sorted_data[length // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = sorted_data[length // 2]
        return round(median, 2)

### Adaptation:
Total number: 2
### Raw Output:
```python
from collections import Counter

class DataStatistics:  
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """


    def mean(self, data):
        pass

    def mode(self, data):
        pass

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            median1 = sorted_data[length // 2]
            median2 = sorted_data[length // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = sorted_data[length // 2]
        return round(median, 2)
```

### Test Code:
class DataStatisticsTestMedian(unittest.TestCase):
    def test_median_1(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 3, 4])
        self.assertEqual(res, 3)

    def test_median_2(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 3, 4, 6])
        self.assertEqual(res, 3.50)

    def test_median_3(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 4, 6, 7])
        self.assertEqual(res, 4.5)

    def test_median_4(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 4, 6, 7, 8])
        self.assertEqual(res, 5)

    def test_median_5(self):
        ds = DataStatistics()
        res = ds.median([2, 5, 1, 4, 6, 7, 8, 9])
        self.assertEqual(res, 5.5)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


