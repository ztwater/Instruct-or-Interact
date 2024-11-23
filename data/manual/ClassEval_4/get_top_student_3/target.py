class AssessmentSystem:
    def get_top_student(self):
        top_student = None
        highest_gpa = 0
        
        for student in self.students:
            gpa = self.get_gpa(student)
            
            if gpa > highest_gpa:
                highest_gpa = gpa
                top_student = student
        
        return top_student