class AssessmentSystem:
    def get_all_students_with_fail_course(students):
        fail_students = []
        for student in students:
            if any(score < 60 for score in student.scores):
                fail_students.append(student)
        return fail_students