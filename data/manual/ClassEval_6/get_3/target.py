class AvgPartition:
    def get(self, index):
        block_size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit

        start_position = index * block_size
        end_position = start_position + block_size

        if index < remainder:
            start_position += index
            end_position += index + 1
        else:
            start_position += remainder
            end_position += remainder

        return self.lst[start_position:end_position]