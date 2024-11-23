class Server:
    def recv(self, info):
        if info["addr"] in self.white_list:
            return info["content"]
        else:
            return False