class Classroom:
    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        """
        formatted_time = datetime.strptime(check_time, '%H:%M').time()
        
        for course in self.courses:
            course_start_time = datetime.strptime(course['start_time'], '%H:%M').time()
            course_end_time = datetime.strptime(course['end_time'], '%H:%M').time()
            
            if course_start_time <= formatted_time <= course_end_time:
                return False
        
        return True