class Server:
    def del_white_list(address, whitelist):
        if address in whitelist:
            whitelist.remove(address)