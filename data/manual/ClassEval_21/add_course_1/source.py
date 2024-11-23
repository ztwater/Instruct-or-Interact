class Classroom:
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)