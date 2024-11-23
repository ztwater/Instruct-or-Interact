class ZipFileProcessor:
    def create_zip_file(file_list, zip_path):
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            for file in file_list:
                zip_file.write(file)
        print(f"Zip file created at {zip_path}")