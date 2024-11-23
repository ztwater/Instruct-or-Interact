class StudentDatabaseProcessor:
    def delete_student_by_name(self, name):
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        # Delete the student from the "students" table
        cursor.execute("DELETE FROM students WHERE name=?", (name,))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()