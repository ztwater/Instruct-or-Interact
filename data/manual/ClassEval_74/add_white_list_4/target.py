class Server:
    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        """
        if addr not in self.white_list:
            self.white_list.append(addr)
            return self.white_list
        else:
            return False