class ExcelProcessor:
    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name:str, Excel file name to read
        :return:list of data, Data in Excel
        """
        try:
            data = pd.read_excel(file_name)
            return data
        except Exception as e:
            print("Error reading Excel file:", str(e))
            return None
