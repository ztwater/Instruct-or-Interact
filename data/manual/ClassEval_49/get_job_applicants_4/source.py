class JobMarketplace:
    def get_job_applicants(candidate_list):
        matching_candidates = []
        
        for candidate in candidate_list:
            if matches_requirements(candidate):
                matching_candidates.append(candidate)
        
        return matching_candidates