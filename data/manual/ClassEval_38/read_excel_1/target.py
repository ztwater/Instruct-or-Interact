class ExcelProcessor:
    def read_excel(self, file_name):
        try:
            data = pd.read_excel(file_name)
            return data
        except Exception as e:
            print("Error reading Excel file:", str(e))
            return None
