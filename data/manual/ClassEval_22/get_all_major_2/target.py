class ClassRegistrationSystem:
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        majors = []
        for student in self.students:
            major = student["major"]
            if major not in majors:
                majors.append(major)
        
        return majors