class DocFileHandler:
    def _get_alignment_value(self, alignment):
        alignment_value = 0
    
        for char in alignment:
            if char == 'left':
                alignment_value += WD_PARAGRAPH_ALIGNMENT.LEFT
            elif char == 'center':
                alignment_value += WD_PARAGRAPH_ALIGNMENT.CENTER
            elif char == 'right':
                alignment_value += WD_PARAGRAPH_ALIGNMENT.RIGHT
    
        return alignment_value