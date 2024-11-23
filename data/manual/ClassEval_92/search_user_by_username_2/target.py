class UserLoginDB:
    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: list of tuples, the rows from the "users" table that match the search criteria.
        """
        query = "SELECT * FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        results = self.cursor.fetchall()
        return results