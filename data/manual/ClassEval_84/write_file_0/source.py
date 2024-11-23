class TextFileProcessor:
    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)