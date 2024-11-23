class Server:
    def show(self, struct_type):
        if struct_type == 'send':
            return self.send_struct
        elif struct_type == 'receive':
            return self.receive_struct
        else:
            return False