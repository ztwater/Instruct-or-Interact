class BitStatusUtil:
    def add(current_status, new_status):
        if not isinstance(current_status, str) or not isinstance(new_status, str):
            raise TypeError("Parameters must be of type str")
        
        return current_status + new_status