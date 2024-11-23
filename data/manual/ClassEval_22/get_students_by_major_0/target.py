class ClassRegistrationSystem:
    def get_students_by_major(self, major):
        students = []
        # Iterate over all students and check if their major matches the given major
        for student in self.students:
            if student['major'] == major:
                students.append(student['name'])
        
        return students