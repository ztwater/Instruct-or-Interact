class ZipFileProcessor:
    def extract_file(zip_file_path, file_name, destination_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extract(file_name, destination_path)