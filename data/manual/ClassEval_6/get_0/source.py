class AvgPartition:
    def get(index, total_size, num_partitions):
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
    
        return block_size, remainder, start_position, end_position