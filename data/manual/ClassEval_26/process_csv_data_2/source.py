class CSVProcessor:
    def process_csv_data(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            title = next(reader)  # Read the first row as the title
            data = list(reader)  # Read the remaining rows as data
    
        return title, data