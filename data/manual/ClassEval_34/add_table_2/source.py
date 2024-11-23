class DocFileHandler:
    def add_table(data):
        # Create a new Word document
        doc = Document()
    
        # Add a table to the document
        table = doc.add_table(rows=len(data), cols=len(data[0]))
    
        # Populate the table with data
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                table.cell(i, j).text = str(value)
    
        # Save the document
        doc.save("document.docx")