class AssessmentSystem:
    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone has a score for this course, or None if nobody has records.
        """
        course_scores = []

        for student in self.students.values():
            if course in student["scores"]:
                course_scores.append(student["scores"][course])

        num_scores = len(course_scores)

        if num_scores == 0:
            return None

        total_score = sum(course_scores)
        average_score = total_score / num_scores
        return average_score