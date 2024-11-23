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
        # Assuming the majors are stored in a list called 'majors'
        majors = ['Computer Science', 'Mathematics', 'Biology', 'Psychology']
        
        return majors
