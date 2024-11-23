class IpUtil:
    def is_valid_ipv6(ip_address):
        """
        Check if the given IP address is a valid IPv6 address.
        :param ip_address:string, the IP address to check
        :return:bool, True if the IP address is valid, False otherwise
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        True
        >>> IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
        False

        """
        # Split the IP address into its individual components
        components = ip_address.split(':')
    
        # Check if the IP address has the correct number of components
        if len(components) != 8:
            return False
    
        # Check if each component is a valid hexadecimal number
        for component in components:
            try:
                int(component, 16)
            except ValueError:
                return False
    
        return True
