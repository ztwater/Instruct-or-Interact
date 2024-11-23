class Classroom:
    def is_free_at(time, classroom_schedule):
        formatted_time = time.strftime('%H:%M')
        if formatted_time in classroom_schedule:
            return False
        else:
            return True