### Method Description:
    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """

### Solution Code:
    def check_course_conflict(self, new_course):
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')

        flag = True
        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M')
            end_time = datetime.strptime(course['end_time'], '%H:%M')
            if start_time <= new_start_time and end_time >= new_start_time:
                flag = False
            if start_time <= new_end_time and end_time >= new_end_time:
                flag = False
        return flag

### Source Code:
    def check_course_conflict(new_course_time, existing_courses):
        for course_time in existing_courses:
            if new_course_time == course_time:
                return True
        return False

### Predicted Code:
    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')

        for course in self.courses:
            course_start_time = datetime.strptime(course['start_time'], '%H:%M')
            course_end_time = datetime.strptime(course['end_time'], '%H:%M')

            if new_start_time == course_start_time or new_end_time == course_end_time:
                return False
            if new_start_time < course_end_time and new_end_time > course_start_time:
                return False

        return True

### Adaptation:
Total number: 17
### Raw Output:
Here is the adapted method `check_course_conflict` in the context of the `Classroom` class:

```
    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')

        for course in self.courses:
            course_start_time = datetime.strptime(course['start_time'], '%H:%M')
            course_end_time = datetime.strptime(course['end_time'], '%H:%M')

            if new_start_time == course_start_time or new_end_time == course_end_time:
                return False
            if new_start_time < course_end_time and new_end_time > course_start_time:
                return False

        return True
```

This method takes a `new_course` dictionary as input, which contains the start time, end time, and name of the new course. It uses the `datetime.strptime` method to convert the start and end time strings into `datetime` objects.

Then, it iterates over each existing course in `self.courses`. For each course, it converts the start and end time strings into `datetime` objects.

It checks for two conditions that indicate a course conflict:
1. If the new course start time is the same as an existing course start time, or the new course end time is the same as an existing course end time, it returns False.
2. If the new course starts before an existing course ends and ends after an existing course starts, it returns False.

If no conflict is found, it returns True at the end.

Note that the `self.courses` list is assumed to contain dictionaries with the same structure as the `new_course` dictionary, with 'start_time', 'end_time', and 'name' keys. The `add_course` method should ensure that the courses are added to `self.courses` in this format.

### Test Code:
class ClassroomTestCheckCourseConflict(unittest.TestCase):
    def test_check_course_conflict_1(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '10:30', 'end_time': '11:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertTrue(result)

    def test_check_course_conflict_2(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '09:30', 'end_time': '10:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

    # have the same boundary time
    # existing_course['end_time'] == new_course['start_time']
    def test_check_course_conflict_3(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '10:00', 'end_time': '11:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

    def test_check_course_conflict_4(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '09:40', 'end_time': '10:40'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

    def test_check_course_conflict_5(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '14:30', 'end_time': '15:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertTrue(result)

    def test_check_course_conflict_6(self):
        classroom = Classroom(1)
        existing_course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(existing_course)
        new_course = {'name': 'SE', 'start_time': '8:30', 'end_time': '9:30'}
        result = classroom.check_course_conflict(new_course)
        self.assertFalse(result)

### Test Output:
# 0 errors, 1 failures in 6 runs.
# errors:
# failures:
#     AssertionError:
#         test_check_course_conflict_3: True is not false


### Dependencies:
# lib_dependencies: datetime
# field_dependencies: self.courses
# method_dependencies: 


