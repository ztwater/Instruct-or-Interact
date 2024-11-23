class DocFileHandler:
    def add_heading(document, text, level):
        # Create a new paragraph
        paragraph = document.add_paragraph()
    
        # Set the alignment of the paragraph to center
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
        # Create a run for the heading text
        run = paragraph.add_run(text)
    
        # Set the font size and bold style for the heading
        run.font.size = Pt(14)
        run.bold = True
    
        # Set the heading level
        paragraph.style = f"Heading {level}"
    