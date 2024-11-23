### Method Description:
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """

### Solution Code:
    def get_all_major(self):
        major_list = []
        for student in self.students:
            if student["major"] not in major_list:
                major_list.append(student["major"])
        return major_list

### Source Code:
    def get_all_major():
        # Assuming the majors are stored in a list called 'majors'
        majors = ['Computer Science', 'Mathematics', 'Biology', 'Psychology']
        
        return majors

### Predicted Code:
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        majors = []
        for student in self.students:
            major = student["major"]
            if major not in majors:
                majors.append(major)
        
        return majors

### Adaptation:
Total number: 4
### Raw Output:
```
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        majors = []
        for student in self.students:
            major = student["major"]
            if major not in majors:
                majors.append(major)
        
        return majors
```

### Test Code:
class ClassRegistrationSystemTestGetMajor(unittest.TestCase):

    def setUp(self):
        self.registration_system = ClassRegistrationSystem()

    def test_get_all_major(self):
        self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"}]

        majors = self.registration_system.get_all_major()

        self.assertEqual(majors, ["Computer Science"])

    def test_get_all_major2(self):
        self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"},
                                             {"name": "Alice", "major": "Mathematics"}]

        majors = self.registration_system.get_all_major()

        self.assertEqual(majors, ["Computer Science", "Mathematics"])

    def test_get_all_major3(self):
        self.registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"},
                                             {"name": "Alice", "major": "Mathematics"},
                                             {"name": "Tom", "major": "Mathematics"},
                                             {"name": "Jerry", "major": "Physics"}]

        majors = self.registration_system.get_all_major()

        self.assertEqual(majors, ["Computer Science", "Mathematics", "Physics"])

### Test Output:
# 0 errors, 0 failures in 3 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.students
# method_dependencies: 


