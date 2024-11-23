class Snake:
    def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.move((1,1))
        >>> snake.eat_food()
        self.length = 2
        self.score = 10
        """
        # Increase the length of the snake by 1
        self.length += 1

        # Increase the score by 100
        self.score += 100

        # Randomly generate a new food position
        while True:
            new_food_position = (random.randint(0, self.SCREEN_WIDTH - 1), random.randint(0, self.SCREEN_HEIGHT - 1))
            if new_food_position not in self.positions:
                break
        self.food_position = new_food_position