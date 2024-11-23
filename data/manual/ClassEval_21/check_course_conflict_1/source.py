class Classroom:
    def check_course_conflict(new_course_time, existing_courses):
        for course_time in existing_courses:
            if new_course_time == course_time:
                return True
        return False