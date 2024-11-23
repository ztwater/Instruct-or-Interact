class DocFileHandler:
    def write_text(self, content, font_size=12, alignment='left'):
        """
        Writes the specified content to a Word document.
        :param content: str, the text content to write.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the write operation is successful, False otherwise.
        """
        document = Document(self.file_path)
        paragraph = document.add_paragraph(content)
        paragraph.runs[0].font.size = Pt(font_size)
        paragraph.alignment = self._get_alignment_value(alignment)
        try:
            document.save(self.file_path)
            return True
        except:
            return False