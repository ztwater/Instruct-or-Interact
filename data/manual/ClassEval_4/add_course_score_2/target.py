class AssessmentSystem:
    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param cource: str, cource name
        :param score: int, cource score
        """
        for student in self.students.values():
            if student['name'] == name:
                student['courses'][course] = score
                break