class Classroom:
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)