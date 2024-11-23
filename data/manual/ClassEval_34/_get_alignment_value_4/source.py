class DocFileHandler:
    def _get_alignment_value(alignment_string):
        alignment_value = 0
        
        for char in alignment_string:
            if char == '-':
                alignment_value += 1
            elif char == '|':
                alignment_value += 2
            elif char == '=':
                alignment_value += 3
        
        return alignment_value