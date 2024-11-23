class IpUtil:
    def is_valid_ipv6(ip_address):
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