class ExcelProcessor:
    def process_excel_data(file_path, sheet_name, column_name):
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Convert the specified column to uppercase
        df[column_name] = df[column_name].str.upper()
        
        # Save the modified DataFrame back to the Excel file
        df.to_excel(file_path, sheet_name=sheet_name, index=False)