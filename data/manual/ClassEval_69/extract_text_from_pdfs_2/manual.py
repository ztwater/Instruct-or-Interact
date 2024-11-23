### Method Description:
    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """

### Solution Code:
    def extract_text_from_pdfs(self):
        pdf_texts = []
        for reader in self.readers:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                pdf_texts.append(page.extract_text())
        return pdf_texts

### Source Code:
    def extract_text_from_pdfs(self):
        extracted_text = []
        
        for reader in self.readers:
            text = ""
            
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
            
            extracted_text.append(text)
        
        return extracted_text

### Predicted Code:
    def extract_text_from_pdfs(self):
        extracted_text = []
        
        for reader in self.readers:
            text = ""
            
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()
            
            extracted_text.append(text)
        
        return extracted_text

### Adaptation:
Total number: 0
### Raw Output:
```python
def extract_text_from_pdfs(self):
    extracted_text = []
    
    for reader in self.readers:
        text = ""
        
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
        
        extracted_text.append(text)
    
    return extracted_text
```

### Test Code:
class PDFHandlerTestMergePdfs(unittest.TestCase):
    def setUp(self) -> None:
        TestPDFHandler.setUpClass()

    def tearDown(self) -> None:
        TestPDFHandler.tearDownClass()

    def test_merge_pdfs(self):
        TestPDFHandler.setUpClass()
        handler = PDFHandler(TestPDFHandler.test_files)
        result = handler.merge_pdfs("merged.pdf")
        self.assertEqual("Merged PDFs saved at merged.pdf", result)
        self.assertTrue(os.path.exists("merged.pdf"))

### Test Output:
# 1 errors, 0 failures in 1 runs.
# errors:
#     NameError:
#         test_merge_pdfs: name 'TestPDFHandler' is not defined
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.readers
# method_dependencies: 


