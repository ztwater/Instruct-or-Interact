class BitStatusUtil:
    def has(current_status, specified_status):
        if isinstance(current_status, str) and isinstance(specified_status, str):
            return specified_status in current_status
        else:
            return False