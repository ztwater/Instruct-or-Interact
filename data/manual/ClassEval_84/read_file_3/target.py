class TextFileProcessor:
    def read_file(self):
        """
        Read and return the content of self.file_path file.
        :return: the same return as the read() method
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
        return content