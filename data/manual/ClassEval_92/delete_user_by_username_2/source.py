class UserLoginDB:
    def delete_user_by_username(username):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
    
        # Delete the user from the "users" table
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    
        # Commit the changes and close the connection
        conn.commit()
        conn.close()