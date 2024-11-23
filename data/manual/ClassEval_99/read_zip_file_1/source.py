class ZipFileProcessor:
    def read_zip_file(file_path):
        try:
            zip_file = zipfile.ZipFile(file_path, 'r')
            file_object = zip_file.open('file_name.txt')
            return file_object
        except FileNotFoundError:
            print("File not found.")
        except zipfile.BadZipFile:
            print("Invalid zip file.")