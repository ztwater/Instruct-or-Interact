class JobMarketplace:
    def remove_job(self, job):
        """
        This function is used to remove positions, and remove the position information from the job_listings list.
        :param job: The position information to be removed, dict.
        :return: None
        """
        for job_listing in self.job_listings:
            if job_listing == job:
                self.job_listings.remove(job_listing)
                break
