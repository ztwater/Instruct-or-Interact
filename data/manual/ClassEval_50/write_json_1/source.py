class JSONProcessor:
    def write_json(data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file)