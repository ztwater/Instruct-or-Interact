class Classroom:
    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts (including two courses have the same boundary time) with other courses, or True otherwise.
        """
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')
        
        for existing_course in self.courses:
            existing_start_time = datetime.strptime(existing_course['start_time'], '%H:%M')
            existing_end_time = datetime.strptime(existing_course['end_time'], '%H:%M')
            
            if new_start_time < existing_end_time and new_end_time > existing_start_time:
                return False
        
        return True
