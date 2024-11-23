class ClassRegistrationSystem:
    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        """
        # Assuming you have a list of classes and their enrollments for each major
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
    
        # Check if the major exists in the classes dictionary
        if major in classes:
            # Get the class with the highest enrollment
            most_popular_class = max(classes[major], key=classes[major].get)
            return most_popular_class
        else:
            return "Major not found"