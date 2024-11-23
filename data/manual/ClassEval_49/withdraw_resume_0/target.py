class JobMarketplace:
    def withdraw_resume(self, resume):
        """
        This function is used to withdraw resumes,and remove the resume information from the resumes list.
        :param resume: The resume information to be removed,dict.
        :return: None
        """
        for r in self.resumes:
            if r == resume:
                self.resumes.remove(r)
                break