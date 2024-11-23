class StudentDatabaseProcessor:
    def insert_student(student):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
    
        # Insert the student into the "students" table
        c.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (student['name'], student['age'], student['grade']))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()