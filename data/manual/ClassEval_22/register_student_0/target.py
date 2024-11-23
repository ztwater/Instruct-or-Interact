class ClassRegistrationSystem:
    def register_student(self, student):
        """
        Register a student to the system, add the student to the students list.
        If the student is already registered, return 0, else return 1.
        """
        if student in [s['name'] for s in self.students]:
            return 0
        else:
            self.students.append({'name': student, 'major': None})
            return 1