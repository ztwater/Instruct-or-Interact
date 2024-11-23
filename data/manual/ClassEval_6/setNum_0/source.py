class AvgPartition:
    def setNum(num, divisor):
        size_of_each_block = num // divisor
        remainder = num % divisor
        return size_of_each_block, remainder