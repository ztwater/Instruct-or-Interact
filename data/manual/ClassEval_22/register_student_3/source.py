class ClassRegistrationSystem:
    def register_student(student, students_list):
        if student in students_list:
            return 0
        else:
            students_list.append(student)
            return 1