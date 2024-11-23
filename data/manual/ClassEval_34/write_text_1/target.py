class DocFileHandler:
    def write_text(self, content, font_size=12, alignment='left'):
        """
        Writes the specified content to a Word document.
        :param content: str, the text content to write.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the write operation is successful, False otherwise.
        """
        document = Document()
        paragraph = document.add_paragraph(content)
        run = paragraph.runs[0]
        run.font.size = Pt(font_size)
        align_value = self._get_alignment_value(alignment)
        paragraph.alignment = align_value
        document.save(self.file_path)
        return True