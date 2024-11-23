class AssessmentSystem:
    def get_gpa(grades):
        total = sum(grades)
        count = len(grades)
        if count == 0:
            return 0
        else:
            return total / count