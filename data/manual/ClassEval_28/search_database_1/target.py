class DatabaseProcessor:
    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        """
        # Connect to the database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        # Execute the query to search for rows with a matching name
        query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(query, (name,))
    
        # Fetch all the matching rows
        rows = cursor.fetchall()
    
        # Close the database connection
        conn.close()
        
        return rows