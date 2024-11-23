class DatabaseProcessor:
    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        # Define the SQL query to create the table
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            {key1} TEXT,
            {key2} INTEGER
        )
        '''
        
        # Execute the SQL query
        cursor.execute(create_table_query)
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()