### Method Description:
    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param cource: str, cource name
        :param score: int, cource score
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        """

### Solution Code:
    def add_course_score(self, name, course, score):
        if name in self.students:
            self.students[name]['courses'][course] = score

### Source Code:
    def add_course_score(self, student_name, course_name, score):
        for student in self.students:
            if student.name == student_name:
                student.courses[course_name] = score
                break

### Predicted Code:
    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param cource: str, cource name
        :param score: int, cource score
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        """
        for student in self.students:
            if self.students[student]['name'] == name:
                self.students[student]['courses'][course] = score
                break

### Adaptation:
Total number: 17
### Raw Output:
class AssessmentSystem:
    """
    This is a class as an student assessment system, which supports add student, add course score, calculate GPA, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dict in assessment system.
        """
        self.students = {}

    def add_student(self, name, grade, major):
        pass

    def get_gpa(self, name):
        pass

    def get_all_students_with_fail_course(self):
        pass

    def get_course_average(self, course):
        pass

    def get_top_student(self):
        pass

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param cource: str, cource name
        :param score: int, cource score
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        """
        for student in self.students:
            if self.students[student]['name'] == name:
                self.students[student]['courses'][course] = score
                break

### Test Code:
class AssessmentSystemTestAddCourseScore(unittest.TestCase):
    def test_add_course_score(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {"Alice": {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}}
        assessment_system.add_course_score("Alice", "Math", 90)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Math"], 90)

    def test_add_course_score_2(self):
        assessment_system = AssessmentSystem()
        assessment_system.students["Alice"] = {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}
        assessment_system.add_course_score("Alice", "Math", 90)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Math"], 90)

    def test_add_course_score_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.students["Alice"] = {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}
        assessment_system.add_course_score("Alice", "Math", 90)
        assessment_system.add_course_score("Alice", "Science", 80)
        assessment_system.add_course_score("Alice", "Math", 95)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Math"], 95)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Science"], 80)

    def test_add_course_score_4(self):
        assessment_system = AssessmentSystem()
        assessment_system.students["Alice"] = {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}
        assessment_system.add_course_score("Alice", "Math", 90)
        assessment_system.add_course_score("Alice", "Science", 80)
        assessment_system.add_course_score("Alice", "Math", 95)
        assessment_system.add_course_score("Alice", "Science", 85)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Math"], 95)
        self.assertEqual(assessment_system.students["Alice"]["courses"]["Science"], 85)

    def test_add_course_score_5(self):
        assessment_system = AssessmentSystem()
        assessment_system.students["Alice"] = {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}
        assessment_system.add_course_score("Bob", "Math", 90)
        self.assertEqual(assessment_system.students["Alice"]["courses"], {})

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.students
# method_dependencies: 


