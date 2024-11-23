### Method Description:
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

### Solution Code:
    def merge_pdfs(self, output_filepath):
        pdf_writer = PyPDF2.PdfWriter()

        for reader in self.readers:
            # reader.getNumPages is deprecated and was removed in PyPDF2 3.0.0. Use len(reader.pages) instead.
            for page_num in range(len(reader.pages)):
                # reader.getPage(pageNumber) is deprecated and was removed in PyPDF2 3.0.0. Use reader.pages[page_number] instead.
                page = reader.pages[page_num]
                # addPage is deprecated and was removed in PyPDF2 3.0.0. Use add_page instead.
                pdf_writer.add_page(page)

        with open(output_filepath, 'wb') as out:
            pdf_writer.write(out)
        return f"Merged PDFs saved at {output_filepath}"

### Source Code:
    def merge_pdfs(self):
        merged_pdf = PyPDF2.PdfFileMerger()
    
        # Iterate over each PDF file handle in self.readers
        for reader in self.readers:
            # Merge the current PDF file with the merged_pdf object
            merged_pdf.append(reader)
    
        # Save the merged PDF to a new file
        merged_pdf.write("merged.pdf")
        merged_pdf.close()

### Predicted Code:
    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        """
        merged_pdf = PyPDF2.PdfFileMerger()
    
        # Iterate over each PDF file handle in self.readers
        for reader in self.readers:
            # Merge the current PDF file with the merged_pdf object
            merged_pdf.append(reader)
    
        # Save the merged PDF to the output file path
        merged_pdf.write(output_filepath)
        merged_pdf.close()
    
        return f"Merged PDFs saved at {output_filepath}"

### Adaptation:
Total number: 8
### Raw Output:
Here is the adapted `merge_pdfs` method in the context of the `PDFHandler` class:

```
def merge_pdfs(self, output_filepath):
    """
    Read files in self.readers which stores handles to multiple PDF files.
    Merge them to one pdf and update the page number, then save in disk.
    :param output_filepath: str, ouput file path to save to
    :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
    """
    merged_pdf = PyPDF2.PdfFileMerger()

    # Iterate over each PDF file handle in self.readers
    for reader in self.readers:
        # Merge the current PDF file with the merged_pdf object
        merged_pdf.append(reader)

    # Save the merged PDF to the output file path
    merged_pdf.write(output_filepath)
    merged_pdf.close()

    return f"Merged PDFs saved at {output_filepath}"
```

### Test Code:
class TestPDFHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_files = ["test1.pdf", "test2.pdf"]
        cls.test_text = ["This is a test1.", "This is a test2."]
        for i in range(2):
            c = canvas.Canvas(cls.test_files[i])
            c.drawString(100, 100, cls.test_text[i])
            c.showPage()
            c.save()

    @classmethod
    def tearDownClass(cls):
        for filename in cls.test_files:
            os.remove(filename)
        os.remove("merged.pdf")

### Test Output:
# 0 errors, 0 failures in 0 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: PyPDF2
# field_dependencies: self.readers
# method_dependencies: 


