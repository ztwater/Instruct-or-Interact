class VectorUtil:
    def similarity(vector_1, vector_2):
        dot_product = np.dot(vector_1, vector_2)
        norm_vector_1 = np.linalg.norm(vector_1)
        norm_vector_2 = np.linalg.norm(vector_2)
        cosine_similarity = dot_product / (norm_vector_1 * norm_vector_2)
        return cosine_similarity
