class VectorUtil:
    def compute_idf_weight_dict(number_dict, total_num):
        idf_weight_dict = {}
        
        for count in number_dict.values():
            idf_weight = math.log((total_num + 1) / (count + 1))
            idf_weight_dict[count] = idf_weight
        
        return idf_weight_dict