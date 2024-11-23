class VectorUtil:
    def compute_idf_weight_dict(total_num, number_dict):
        idf_weight_dict = {}

        for key, count in number_dict.items():
            idf_weight = math.log((total_num + 1) / (count + 1))
            idf_weight_dict[key] = idf_weight
        
        return idf_weight_dict