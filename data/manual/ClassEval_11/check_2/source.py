class BitStatusUtil:
    def check(*args):
        for arg in args:
            if arg < 0 or arg % 2 != 0:
                raise ValueError("Parameters must be greater than or equal to 0 and even.")