class AssessmentSystem:
    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this student has courses grade, return average grade(float)
                    or None otherwise
        """
        if name in self.students:
            grades = self.students[name]['courses'].values()
            total = sum(grades)
            count = len(grades)
            if count == 0:
                return None
            else:
                return total / count
        else:
            return None