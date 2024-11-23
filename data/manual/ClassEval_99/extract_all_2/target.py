class ZipFileProcessor:
    def extract_all(self, output_path):
        files = os.listdir(self.file_name)
    
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(self.file_name, file)
    
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(output_path)
    
                os.remove(zip_path)