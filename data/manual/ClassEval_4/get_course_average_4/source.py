class AssessmentSystem:
    def get_course_average(course_scores):
        total_score = 0
        num_scores = len(course_scores)
        
        if num_scores == 0:
            return 0
        
        for score in course_scores:
            total_score += score
        
        average_score = total_score / num_scores
        return average_score