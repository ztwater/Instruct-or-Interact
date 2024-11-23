class ClassRegistrationSystem:
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """
        majors = []
        for student in self.students:
            major = student["major"]
            if major not in majors:
                majors.append(major)
        return majors