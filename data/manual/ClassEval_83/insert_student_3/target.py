class StudentDatabaseProcessor:
    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)",
                  (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
        conn.commit()
        conn.close()
