class JSONProcessor:
    def process_json(file_path, key_to_remove):
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Remove the specified key from the data
        if key_to_remove in data:
            del data[key_to_remove]
        
        # Write the modified data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file)