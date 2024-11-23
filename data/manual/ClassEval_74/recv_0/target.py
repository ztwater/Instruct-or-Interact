class Server:
    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the information; otherwise, return False
        """
        address = info.get("addr")
        content = info.get("content")
    
        if address in self.white_list:
            return content
        else:
            return False