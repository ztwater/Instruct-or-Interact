class CSVProcessor:
    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            title = next(csv_reader)  # Get the title from the first row
            data = list(csv_reader)  # Get the data from the remaining rows
        return title, data
