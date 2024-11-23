class JobMarketplace:
    def get_job_applicants(self, job):
        matching_candidates = []
        
        for candidate in self.resumes:
            if self.matches_requirements(candidate, job):
                matching_candidates.append(candidate)
        
        return matching_candidates
    