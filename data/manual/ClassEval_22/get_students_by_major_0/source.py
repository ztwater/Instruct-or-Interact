class ClassRegistrationSystem:
    def get_students_by_major(major):
        students = []
        # Assuming you have a list of students with their majors
        all_students = [
            {'name': 'John', 'major': 'Computer Science'},
            {'name': 'Jane', 'major': 'Mathematics'},
            {'name': 'Mike', 'major': 'Computer Science'},
            {'name': 'Sarah', 'major': 'Physics'},
            {'name': 'Emily', 'major': 'Mathematics'}
        ]
        
        # Iterate over all students and check if their major matches the given major
        for student in all_students:
            if student['major'] == major:
                students.append(student['name'])
        
        return students