class ExcelProcessor:
    def write_excel(file_path, data):
        # Create a DataFrame from the data
        df = pd.DataFrame(data)
        
        # Write the DataFrame to the Excel file
        df.to_excel(file_path, index=False)