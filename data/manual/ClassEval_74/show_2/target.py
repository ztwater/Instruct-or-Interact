class Server:
    def show(self, struct_type):
        """
        Returns struct of the specified type
        :param struct_type: string, the type of struct to be returned, which can be 'send' or 'receive'
        :return: if struct_type is equal to 'send' or 'receive', return the corresponding struct; otherwise, return False
        """
        if struct_type == 'send':
            return self.send_struct
        elif struct_type == 'receive':
            return self.receive_struct
        else:
            return False