class ZipFileProcessor:
    def extract_all(path):
        # Get a list of all files in the specified path
        files = os.listdir(path)
    
        # Iterate over each file in the path
        for file in files:
            # Check if the file is a zip file
            if file.endswith('.zip'):
                # Create the full path to the zip file
                zip_path = os.path.join(path, file)
    
                # Open the zip file
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # Extract all files in the zip file to the specified path
                    zip_ref.extractall(path)
    
                # Remove the zip file after extraction
                os.remove(zip_path)