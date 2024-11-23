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