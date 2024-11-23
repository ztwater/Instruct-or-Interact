class AvgPartition:
    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        """
        num = len(self.lst)
        divisor = self.limit
        size_of_each_block = num // divisor
        remainder = num % divisor
        return size_of_each_block, remainder