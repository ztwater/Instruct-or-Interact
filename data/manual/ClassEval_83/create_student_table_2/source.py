class StudentDatabaseProcessor:
    def create_student_table():
        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Create the "students" table if it does not exist
        c.execute('''CREATE TABLE IF NOT EXISTS students
                     (ID INT, name TEXT, age INT, gender TEXT, grade INT)''')
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()