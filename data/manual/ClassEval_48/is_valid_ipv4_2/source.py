class IpUtil:
    def is_valid_ipv4(ip_address):
        # Split the IP address into its components
        components = ip_address.split('.')
    
        # Check if the IP address has exactly 4 components
        if len(components) != 4:
            return False
    
        # Check if each component is a valid integer between 0 and 255
        for component in components:
            try:
                # Convert the component to an integer
                value = int(component)
                # Check if the value is between 0 and 255
                if value < 0 or value > 255:
                    return False
            except ValueError:
                # If the component cannot be converted to an integer, it is not valid
                return False
    
        # If all checks pass, the IP address is valid
        return True