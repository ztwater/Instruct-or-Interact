class JobMarketplace:
    def remove_job(self, job):
        for job_listing in self.job_listings:
            if job_listing == job:
                self.job_listings.remove(job_listing)
                break