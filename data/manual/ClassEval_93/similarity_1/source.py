class VectorUtil:
    def similarity(vector1, vector2):
        dot_product = np.dot(vector1, vector2)
        norm_vector1 = np.linalg.norm(vector1)
        norm_vector2 = np.linalg.norm(vector2)
        cosine_similarity = dot_product / (norm_vector1 * norm_vector2)
        return cosine_similarity