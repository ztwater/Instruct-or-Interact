class Server:
    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the information; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
        if info["addr"] in self.white_list:
            return info["content"]
        else:
            return False