class IPAddress:
    def is_valid(ip_address):
        # Split the IP address into four parts
        parts = ip_address.split('.')
        
        # Check if there are exactly four parts
        if len(parts) != 4:
            return False
        
        # Check each part of the IP address
        for part in parts:
            # Check if the part is a valid decimal number
            if not part.isdigit():
                return False
            
            # Convert the part to an integer
            num = int(part)
            
            # Check if the number is within the valid range
            if num < 0 or num > 255:
                return False
        
        # If all checks pass, the IP address is valid
        return True