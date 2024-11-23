class DocFileHandler:
    def add_heading(self, heading, level=1):
        """
        Adds a heading to the Word document.
        :param heading: str, the text of the heading.
        :param level: int, optional, the level of the heading (1, 2, 3, etc.; default is 1).
        :return: bool, True if the heading is successfully added, False otherwise.
        """
        # Create a new paragraph
        paragraph = self.document.add_paragraph()
    
        # Set the alignment of the paragraph to center
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
        # Create a run for the heading text
        run = paragraph.add_run(heading)
    
        # Set the font size and bold style for the heading
        run.font.size = Pt(14)
        run.bold = True
    
        # Set the heading level
        paragraph.style = f"Heading {level}"