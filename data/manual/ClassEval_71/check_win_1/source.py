class PushBoxGame:
    def check_win(boxes, targets):
        for box in boxes:
            if box not in targets:
                return False
        return True