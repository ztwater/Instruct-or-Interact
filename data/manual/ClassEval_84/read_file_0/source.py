class TextFileProcessor:
    def read_file(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        return content