class StudentDatabaseProcessor:
    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        # Delete the student from the table
        cursor.execute("DELETE FROM students WHERE name=?", (name,))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()