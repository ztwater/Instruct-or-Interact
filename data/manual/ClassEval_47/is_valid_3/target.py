class IPAddress:
    def is_valid(self):
        parts = self.ip_address.split('.')
    
        if len(parts) != 4:
            return False
    
        for part in parts:
            if not part.isdigit():
                return False
    
            num = int(part)
    
            if num < 0 or num > 255:
                return False
    
        return True