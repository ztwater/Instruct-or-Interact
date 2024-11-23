class JobMarketplace:
    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes, and add the resume information to the resumes list.
        :param name: The name of the resume, str.
        :param skills: The skills of the resume, list.
        :param experience: The experience of the resume, str.
        :return: None
        """
        resume_info = {'name': name, 'skills': skills, 'experience': experience}
        self.resumes.append(resume_info)