class DocFileHandler:
    def add_heading(self, heading, level=1):
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
    
        return True