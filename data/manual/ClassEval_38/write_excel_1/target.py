class ExcelProcessor:
    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        """
        # Create a DataFrame from the data
        df = pd.DataFrame(data)
        
        # Write the DataFrame to the Excel file
        df.to_excel(file_name, index=False)
        
        return 1