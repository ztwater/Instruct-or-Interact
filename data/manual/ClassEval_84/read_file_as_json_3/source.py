class TextFileProcessor:
    def read_file_as_json(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data