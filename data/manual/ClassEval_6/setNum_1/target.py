class AvgPartition:
    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.setNum()
        (2, 0)

        """
        size_of_each_block = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return size_of_each_block, remainder