class TextFileProcessor:
    def process_file(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
            filtered_content = ''.join(filter(str.isalpha, content))
            return filtered_content