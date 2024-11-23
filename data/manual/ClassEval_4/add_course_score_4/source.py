class AssessmentSystem:
    def add_course_score(self, student_name, course_name, score):
        for student in self.students:
            if student.name == student_name:
                student.courses[course_name] = score
                break