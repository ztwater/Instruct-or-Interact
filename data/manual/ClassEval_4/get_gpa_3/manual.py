### Method Description:
    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0

        """

### Solution Code:
    def get_gpa(self, name):
        if name in self.students and self.students[name]['courses']:
            return sum(self.students[name]['courses'].values()) / len(self.students[name]['courses'])
        else:
            return None

### Source Code:
    def get_gpa(grades):
        total = sum(grades)
        count = len(grades)
        if count == 0:
            return 0
        else:
            return total / count

### Predicted Code:
    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """
        if name in self.students:
            grades = self.students[name]
            total = sum(grades)
            count = len(grades)
            if count == 0:
                return None
            else:
                return total / count
        else:
            return None

### Adaptation:
Total number: 9
### Raw Output:
```
    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """
        if name in self.students:
            grades = self.students[name]
            total = sum(grades)
            count = len(grades)
            if count == 0:
                return None
            else:
                return total / count
        else:
            return None
```

### Test Code:
class AssessmentSystemTestGetGPA(unittest.TestCase):
    def test_get_gpa_1(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90, 'Science': 80}}}
        self.assertEqual(assessment_system.get_gpa("Alice"), 85.0)


    # No such student
    def test_get_gpa_2(self):
        assessment_system = AssessmentSystem()
        self.assertEqual(assessment_system.get_gpa('Alice'), None)

    # student don't have any scores
    def test_get_gpa_3(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {}}}
        self.assertEqual(assessment_system.get_gpa('Alice'), None)

    def test_get_gpa_4(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90}}}
        self.assertEqual(assessment_system.get_gpa('Bob'), None)

    def test_get_gpa_5(self):
        assessment_system = AssessmentSystem()
        assessment_system.students = {'Alice': {'name': 'Alice', 'grade': 3, 'major': 'Mathematics', 'courses': {'Mathematics': 90}}}
        self.assertEqual(assessment_system.get_gpa('Alice'), 90.0)

### Test Output:
# 3 errors, 0 failures in 5 runs.
# errors:
#     TypeError:
#         test_get_gpa_1: unsupported operand type(s) for +: 'int' and 'str'
#         test_get_gpa_3: unsupported operand type(s) for +: 'int' and 'str'
#         test_get_gpa_5: unsupported operand type(s) for +: 'int' and 'str'
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.students
# method_dependencies: 


