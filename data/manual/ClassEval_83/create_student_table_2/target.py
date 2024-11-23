class StudentDatabaseProcessor:
    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        
        # Create the "students" table if it does not exist
        c.execute('''CREATE TABLE IF NOT EXISTS students
                     (ID INT, name TEXT, age INT, gender TEXT, grade INT)''')
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()