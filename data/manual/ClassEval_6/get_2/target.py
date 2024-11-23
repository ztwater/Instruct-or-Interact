class AvgPartition:
    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :param index: the index of the partition,int.
        :return: the corresponding block, list.
        >>> a = AvgPartition([1, 2, 3, 4], 2)
        >>> a.get(0)
        [1, 2]

        """
        total_size = len(self.lst)
        num_partitions = self.limit
        
        block_size = total_size // num_partitions
        remainder = total_size % num_partitions
    
        start_position = index * block_size
        end_position = start_position + block_size
    
        if index < remainder:
            start_position += index
            end_position += index + 1
        else:
            start_position += remainder
            end_position += remainder
    
        return self.lst[start_position:end_position]