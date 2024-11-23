class MetricsCalculator2:
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