class Snake:
    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        snake_positions = [pos for pos in self.positions]
        grid_size = self.SCREEN_WIDTH // self.BLOCK_SIZE
        while True:
            food_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
            if food_position not in snake_positions:
                self.food_position = food_position
                return