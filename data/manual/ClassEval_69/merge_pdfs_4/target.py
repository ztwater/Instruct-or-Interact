class PDFHandler:
    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        merged_pdf = PyPDF2.PdfFileMerger()
    
        # Iterate over each PDF file handle in self.readers
        for reader in self.readers:
            # Merge the current PDF file with the merged_pdf object
            merged_pdf.append(reader)
    
        # Save the merged PDF to the specified output file
        merged_pdf.write(output_filepath)
        merged_pdf.close()
    
        return f"Merged PDFs saved at {output_filepath}"