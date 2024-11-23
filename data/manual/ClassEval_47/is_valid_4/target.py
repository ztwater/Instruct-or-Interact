class IPAddress:
    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """
        # Split the IP address into four parts
        parts = self.ip_address.split('.')
        
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

