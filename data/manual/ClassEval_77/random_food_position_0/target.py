class Snake:
    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        while True:
            food_position = (random.randint(0, self.SCREEN_WIDTH-1), random.randint(0, self.SCREEN_HEIGHT-1))
            if food_position not in self.positions:
                self.food_position = food_position
                break