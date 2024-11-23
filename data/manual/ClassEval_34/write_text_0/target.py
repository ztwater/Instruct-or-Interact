class DocFileHandler:
    def write_text(self, content, font_size=12, alignment='left'):
        document = Document()
        paragraph = document.add_paragraph()
        run = paragraph.add_run(content)
        run.font.size = Pt(font_size)
        run.alignment = self._get_alignment_value(alignment)
        document.save(self.file_path)
        return True