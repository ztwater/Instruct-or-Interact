class IPAddress:
    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        """
        if not self.is_valid():
            return ''

        octets = self.get_octets()
        binary_ip = '.'.join(bin(int(octet))[2:].zfill(8) for octet in octets)

        return binary_ip