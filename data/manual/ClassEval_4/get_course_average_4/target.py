class AssessmentSystem:
    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        total_score = 0
        num_scores = 0
    
        if course in self.students:
            course_scores = self.students[course]
            num_scores = len(course_scores)
    
            if num_scores == 0:
                return None
    
            for score in course_scores:
                total_score += score
    
            average_score = total_score / num_scores
            return average_score
    
        return None