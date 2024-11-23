class Classroom:
    def is_free_at(self, check_time):
        formatted_time = datetime.strptime(check_time, '%H:%M')
        formatted_time = formatted_time.strftime('%H:%M')
        for course in self.courses:
            if formatted_time >= course['start_time'] and formatted_time < course['end_time']:
                return False
        return True