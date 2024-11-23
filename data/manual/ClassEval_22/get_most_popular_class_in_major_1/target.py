class ClassRegistrationSystem:
    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        """
        classes = {
            'Computer Science': {
                'CS101': 50,
                'CS201': 75,
                'CS301': 100
            },
            'Mathematics': {
                'MATH101': 60,
                'MATH201': 80,
                'MATH301': 90
            },
            'Biology': {
                'BIO101': 70,
                'BIO201': 85,
                'BIO301': 95
            }
        }
    
        if major in classes:
            if major in self.students_registration_classes.values():
                registrations = self.students_registration_classes.values()
                major_enrollments = []
                for student_classes in registrations:
                    for class_name in student_classes:
                        if class_name in classes[major]:
                            major_enrollments.append(classes[major][class_name])
                if major_enrollments:
                    most_popular_class = max(classes[major], key=classes[major].get)
                    return most_popular_class
                else:
                    return "No enrollments found for this major"
            else:
                return "No students registered for this major"
        else:
            return "Major not found"