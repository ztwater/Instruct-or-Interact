class StudentDatabaseProcessor:
    def search_student_by_name(name):
        # Connect to the database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
    
        # Execute the query to search for the student by name
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        result = cursor.fetchall()
    
        # Close the database connection
        connection.close()
    
        # Return the search result
        return result