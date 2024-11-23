class UserLoginDB:
    def insert_user(user_id, username, email):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
    
        c.execute("INSERT INTO users (user_id, username, email) VALUES (?, ?, ?)", (user_id, username, email))
    
        conn.commit()
        conn.close()