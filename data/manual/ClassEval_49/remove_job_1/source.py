class JobMarketplace:
    def remove_job(job_listings, position):
        for job in job_listings:
            if job['position'] == position:
                job_listings.remove(job)
                break