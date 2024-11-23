class AssessmentSystem:
    def add_course_score(self, name, course, score):
        for student in self.students.values():
            if student['name'] == name:
                student['courses'][course] = score
                break