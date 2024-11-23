class VectorUtil:
    def n_similarity(vectors1, vectors2):
        # Convert the sets of vectors to numpy arrays
        vectors1 = np.array(vectors1)
        vectors2 = np.array(vectors2)
        
        # Compute the cosine similarity between the two sets of vectors
        similarity = cosine_similarity(vectors1, vectors2)
        
        return similarity