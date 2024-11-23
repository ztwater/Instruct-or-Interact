class UserLoginDB:
    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        # Delete the user from the "users" table
        self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    
        # Commit the changes and close the connection
        self.connection.commit()