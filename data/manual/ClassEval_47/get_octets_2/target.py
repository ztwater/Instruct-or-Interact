class IPAddress:
    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """
        octets = self.ip_address.split(".")
        if len(octets) != 4:
            return []
        for octet in octets:
            if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
                return []
        return octets