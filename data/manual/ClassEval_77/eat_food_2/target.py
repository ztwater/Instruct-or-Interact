class Snake:
    def eat_food(self):
        # Increase the length of the snake by 1
        self.length += 1
        
        # Increase the score by 100
        self.score += 100
        
        # Randomly generate a new food position
        while True:
            new_food_position = self.random_food_position()
            if new_food_position not in self.positions:
                self.food_position = new_food_position
                break