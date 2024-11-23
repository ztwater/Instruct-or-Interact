class Snake:
    def random_food_position(snake_positions, grid_size):
        while True:
            food_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
            if food_position not in snake_positions:
                return food_position