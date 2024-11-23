class ExcelProcessor:
    def process_excel_data(self, N, save_file_name):
        # Read the Excel file into a DataFrame
        df = self.read_excel(save_file_name)
        
        # Convert the specified column to uppercase
        column_name = df.columns[N-1]
        df[column_name] = df[column_name].str.upper()
        
        # Save the modified DataFrame back to the Excel file
        self.write_excel(df, save_file_name)
        
        # Return the return value of write_excel and the saved file name
        return self.write_excel(df, save_file_name), save_file_name