class Server:
    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """
        address = info["addr"]
        content = info["content"]
        # Code to send information goes here
        print("Sending information to:", address)
        print("Content:", content)
        self.send_struct = info