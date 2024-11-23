class JobMarketplace:
    def withdraw_resume(resumes, resume_id):
        for resume in resumes:
            if resume['id'] == resume_id:
                resumes.remove(resume)
                break