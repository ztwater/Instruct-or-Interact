class Classroom:
    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        """
        formatted_time = datetime.strptime(check_time, '%H:%M')
        formatted_time = formatted_time.strftime('%H:%M')

        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M')
            start_time = start_time.strftime('%H:%M')
            end_time = datetime.strptime(course['end_time'], '%H:%M')
            end_time = end_time.strftime('%H:%M')
            
            if start_time <= formatted_time <= end_time:
                return False  # Time conflicts with a course
            
        return True  # Time is free