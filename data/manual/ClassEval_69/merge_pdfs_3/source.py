class PDFHandler:
    def merge_pdfs(self):
        merged_pdf = PyPDF2.PdfFileMerger()
    
        # Iterate over each PDF file handle in self.readers
        for reader in self.readers:
            # Merge the current PDF file with the merged_pdf object
            merged_pdf.append(reader)
    
        # Save the merged PDF to a new file
        merged_pdf.write("merged.pdf")
        merged_pdf.close()