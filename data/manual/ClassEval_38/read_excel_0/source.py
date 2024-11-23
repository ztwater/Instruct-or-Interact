class ExcelProcessor:
    def read_excel(file_path):
        try:
            data = pd.read_excel(file_path)
            return data
        except Exception as e:
            print("Error reading Excel file:", str(e))
            return None