class AssessmentSystem:
    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        total_score = 0
        num_scores = 0
        
        for student in self.students.values():
            if course in student['courses']:
                total_score += student['courses'][course]
                num_scores += 1
        
        if num_scores == 0:
            return None
        
        average_score = total_score / num_scores
        return average_score