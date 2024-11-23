class JobMarketplace:
    def remove_job(self, job):
        """
        This function is used to remove positions, and remove the position information from the job_listings list.
        :param job: The position information to be removed, dict.
        :return: None
        """
        for listed_job in self.job_listings:
            if listed_job == job:
                self.job_listings.remove(listed_job)
                break