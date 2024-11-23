class CSVProcessor:
    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of the file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        """
        with open(save_file_name, 'r') as file:
            reader = csv.reader(file)
            title = next(reader)  # Read the first row as the title
            
            processed_data = []
            for row in reader:
                processed_data.append(row[N].upper())  # Only remain the Nth column data and capitalize them
            
        processed_file_name = save_file_name.split('.')[0] + '_process.csv'  # Add '_process' suffix after old file name
        self.write_csv([title, processed_data], processed_file_name)  # Store the title and new data into a new csv file
        
        return 1