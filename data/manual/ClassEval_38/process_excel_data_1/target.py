class ExcelProcessor:
    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
        # Read the Excel file into a DataFrame
        df = self.read_excel(save_file_name)
        
        # Get the column name based on the serial number
        column_name = df.columns[N-1]
        
        # Convert the specified column to uppercase
        df[column_name] = df[column_name].str.upper()
        
        # Save the modified DataFrame back to the Excel file
        success = self.write_excel(df, save_file_name)
        
        # Return the return value of write_excel and the saved file name
        return success, save_file_name