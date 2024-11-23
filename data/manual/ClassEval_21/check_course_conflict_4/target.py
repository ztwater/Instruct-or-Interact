class Classroom:
    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        for course in self.courses:
            if (new_course['start_time'] >= course['start_time'] and new_course['start_time'] <= course['end_time']) or (new_course['end_time'] >= course['start_time'] and new_course['end_time'] <= course['end_time']):
                return False
        return True