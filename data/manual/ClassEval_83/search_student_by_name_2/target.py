class StudentDatabaseProcessor:
    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """

        # Connect to the database
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        # Execute the query to search for the student by name
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        result = cursor.fetchall()

        # Close the database connection
        connection.close()

        # Return the search result
        return result