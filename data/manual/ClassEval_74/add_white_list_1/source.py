class Server:
    def add_white_list(address, whitelist):
        if address not in whitelist:
            whitelist.append(address)