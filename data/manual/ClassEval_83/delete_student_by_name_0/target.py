class StudentDatabaseProcessor:
    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> processor.delete_student_by_name("John")
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        cursor.execute("DELETE FROM students WHERE name=?", (name,))
    
        conn.commit()
        conn.close()