class ClassRegistrationSystem:
    def get_students_by_major(self, major):
        students = []
        for student in self.students:
            if student['major'] == major:
                students.append(student['name'])
        return students