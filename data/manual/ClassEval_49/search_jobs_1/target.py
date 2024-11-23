class JobMarketplace:
    def search_jobs(self, criteria):
        matching_positions = []
        
        for position in self.job_listings:
            if all(req in position["requirements"] for req in criteria):
                matching_positions.append(position)
        
        return matching_positions