class MetricsCalculator2:
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
        reciprocal_ranks = []
        if isinstance(data, tuple):
            data = [data]
        
        for query_results, ground_truth_num in data:
            for i, result in enumerate(query_results):
                if result == 1:
                    reciprocal_ranks.append(1 / (i + 1))
                    break
        
        if len(reciprocal_ranks) == 0:
            return 0
        
        return sum(reciprocal_ranks) / len(reciprocal_ranks)