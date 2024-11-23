class TextFileProcessor:
    def read_file(self):
        """
        Read and return the content of self.file_path file.
        :return: file content as str
        """
        with open(self.file_path, 'r') as file:
            content = file.read()
        return content
