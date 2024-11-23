class DocFileHandler:
    def _get_alignment_value(self, alignment):
        alignment_value = 0
            
        if alignment == 'left':
            alignment_value = WD_PARAGRAPH_ALIGNMENT.LEFT
        elif alignment == 'center':
            alignment_value = WD_PARAGRAPH_ALIGNMENT.CENTER
        elif alignment == 'right':
            alignment_value = WD_PARAGRAPH_ALIGNMENT.RIGHT
            
        return alignment_value