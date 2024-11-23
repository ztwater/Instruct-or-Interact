class ClassRegistrationSystem:
    def register_class(self, student_name, class_name):
        """
        Register a class to the student.
        :param student_name: str
        :param class_name: str
        :return: a list of class names that the student has registered
        """
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        
        return self.students_registration_classes[student_name]