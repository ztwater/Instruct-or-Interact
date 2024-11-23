class PDFHandler:
    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        extracted_text = []
        
        for reader in self.readers:
            text = ""
            
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
            
            extracted_text.append(text)
        
        return extracted_text