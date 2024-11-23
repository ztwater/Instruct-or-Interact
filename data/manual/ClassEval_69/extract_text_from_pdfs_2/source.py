class PDFHandler:
    def extract_text_from_pdfs(self):
        extracted_text = []
        
        for reader in self.readers:
            text = ""
            
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
            
            extracted_text.append(text)
        
        return extracted_text