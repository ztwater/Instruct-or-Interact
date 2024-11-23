class Server:
    def recv(address, content, whitelist):
        if address in whitelist:
            return content
        else:
            return None