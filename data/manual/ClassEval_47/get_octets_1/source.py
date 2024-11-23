class IPAddress:
    def get_octets(ip_address):
        octets = ip_address.split(".")
        if len(octets) != 4:
            return []
        for octet in octets:
            if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
                return []
        return octets