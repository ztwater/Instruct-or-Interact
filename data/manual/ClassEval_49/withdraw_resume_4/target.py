class JobMarketplace:
    def withdraw_resume(self, resume):
        for r in self.resumes:
            if r == resume:
                self.resumes.remove(r)
                break