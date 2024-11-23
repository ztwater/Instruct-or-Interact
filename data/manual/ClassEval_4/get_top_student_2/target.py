class AssessmentSystem:
    def get_top_student(self):
        top_student = None
        highest_gpa = 0
        
        for student in self.students.values():
            gpa = self.get_gpa(student.name)
            
            if gpa > highest_gpa:
                highest_gpa = gpa
                top_student = student.name
        
        return top_student