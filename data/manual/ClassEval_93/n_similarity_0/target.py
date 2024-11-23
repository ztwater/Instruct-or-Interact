class VectorUtil:
    def n_similarity(vector_list_1, vector_list_2):
        # Convert the sets of vectors to numpy arrays
        vectors1 = np.array(vector_list_1)
        vectors2 = np.array(vector_list_2)
        
        # Compute the cosine similarity between the two sets of vectors
        similarity = matutils.cosine_similarity(vectors1, vectors2)
        
        return similarity