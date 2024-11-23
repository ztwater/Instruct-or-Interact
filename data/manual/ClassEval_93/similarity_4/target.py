class VectorUtil:
    def similarity(vector_1, vector_2):
        dot_product = np.dot(vector_1, vector_2)
        norm_vector1 = np.linalg.norm(vector_1)
        norm_vector2 = np.linalg.norm(vector_2)
        cosine_similarity = dot_product / (norm_vector1 * norm_vector2)
        return cosine_similarity
        