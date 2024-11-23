### Method Description:
    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """

### Solution Code:
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

### Source Code:
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

### Predicted Code:
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

### Adaptation:
Total number: 0
### Raw Output:
```
def remove_course(self, course):
    if course in self.courses:
        self.courses.remove(course)
```

### Test Code:
class ClassroomTestRemoveCourse(unittest.TestCase):
    def test_remove_course_1(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_2(self):
        classroom = Classroom(1)
        course = {'name': 'Chinese', 'start_time': '10:00', 'end_time': '11:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_3(self):
        classroom = Classroom(1)
        course = {'name': 'English', 'start_time': '11:00', 'end_time': '12:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_4(self):
        classroom = Classroom(1)
        course = {'name': 'Art', 'start_time': '14:00', 'end_time': '15:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_5(self):
        classroom = Classroom(1)
        course = {'name': 'P.E.', 'start_time': '15:00', 'end_time': '16:00'}
        classroom.add_course(course)
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

    def test_remove_course_6(self):
        classroom = Classroom(1)
        course = {'name': 'math', 'start_time': '09:00', 'end_time': '10:00'}
        classroom.remove_course(course)
        self.assertNotIn(course, classroom.courses)

### Test Output:
# 0 errors, 0 failures in 6 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.courses
# method_dependencies: 


