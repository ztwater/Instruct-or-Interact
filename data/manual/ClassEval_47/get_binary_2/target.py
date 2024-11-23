class IPAddress:
    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return:string
        """
        octets = self.ip_address.split('.')
        
        if len(octets) != 4:
            return ''
        
        for octet in octets:
            if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
                return ''
        
        binary_ip = '.'.join(bin(int(octet))[2:].zfill(8) for octet in octets)
        
        return binary_ip