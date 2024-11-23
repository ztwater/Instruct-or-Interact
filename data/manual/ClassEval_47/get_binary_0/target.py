class IPAddress:
    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        """
        # Split the IP address into its octets
        octets = self.ip_address.split('.')
        
        # Check if the IP address is valid
        if len(octets) != 4:
            return ''
        
        for octet in octets:
            # Check if each octet is a valid number between 0 and 255
            if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
                return ''
        
        # Convert each octet to its binary form and join them with dots
        binary_ip = '.'.join(bin(int(octet))[2:].zfill(8) for octet in octets)
        
        return binary_ip