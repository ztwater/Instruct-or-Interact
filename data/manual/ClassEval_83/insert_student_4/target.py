class StudentDatabaseProcessor:
    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
    
        # Insert the student into the "students" table
        c.execute("INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)", 
                  (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()