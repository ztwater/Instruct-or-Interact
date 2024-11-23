class JobMarketplace:
    def search_jobs(self, criteria):
        """
        This function is used to search for positions, and return the position information that meets the requirements.
        :param criteria: The requirements of the position, list.
        :return: The position information that meets the requirements, list.
        """
        matching_positions = []
        
        for position in self.job_listings:
            if all(req in position['requirements'] for req in criteria):
                matching_positions.append(position)
        
        return matching_positions