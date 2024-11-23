class ZipFileProcessor:
    def create_zip_file(self, files, output_file_name):
        """
        Compress the specified file list into a zip file and place it in the specified path
        :param files:list of string, List of files to compress
        :param output_file_name: string, Specified output path
        :return:True or False, representing whether the compression operation was successful
        >>> zfp = ZipFileProcessor("aaa.zip")
        >>> zfp.create_zip_file(["bbb.txt", "ccc,txt", "ddd.txt"], "output/bcd")
        """
        with zipfile.ZipFile(self.file_name, 'w') as zip_file:
            for file in files:
                zip_file.write(file)
        print(f"Zip file created at {self.file_name}")