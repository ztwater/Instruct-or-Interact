class MetricsCalculator2:
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
        # Compute the Average Precision (AP) for each data point
        ap_list = []
        for data_point in data:
            # Compute the precision and recall for the data point
            precision = compute_precision(data_point)
            recall = compute_recall(data_point)
            
            # Compute the Average Precision (AP) for the data point
            ap = precision * recall
            
            # Add the AP to the list of APs
            ap_list.append(ap)
        
        # Compute the Mean Average Precision (MAP) by taking the mean of APs
        map_score = np.mean(ap_list)
        
        return map_score