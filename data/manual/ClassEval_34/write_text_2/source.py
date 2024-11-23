class DocFileHandler:
    def write_text(content, filename):
        document = Document()
        document.add_paragraph(content)
        document.save(filename)