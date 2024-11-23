class StudentDatabaseProcessor:
    def delete_student_by_name(name):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
    
        # Delete the student from the table
        cursor.execute("DELETE FROM students WHERE name=?", (name,))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()