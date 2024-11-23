class CSVProcessor:
    def read_csv(file_name):
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            title = next(csv_reader)  # Get the title from the first row
            data = list(csv_reader)  # Get the data from the remaining rows
        return title, data