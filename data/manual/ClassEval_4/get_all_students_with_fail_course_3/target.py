class AssessmentSystem:
    def get_all_students_with_fail_course(self):
        fail_students = []
        for student in self.students.values():
            if any(score < 60 for score in student.scores.values()):
                fail_students.append(student.name)
        return fail_students