class Snake:
    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        """

        # Calculate the new position of the snake's head based on the direction
        if direction == "up":
            new_head = (self.positions[0][0], self.positions[0][1] - 1)
        elif direction == "down":
            new_head = (self.positions[0][0], self.positions[0][1] + 1)
        elif direction == "left":
            new_head = (self.positions[0][0] - 1, self.positions[0][1])
        elif direction == "right":
            new_head = (self.positions[0][0] + 1, self.positions[0][1])

        # Check if the new position of the snake's head is equal to the position of the food
        if new_head == self.food_position:
            # If yes, eat the food and increase the length of the snake by one
            self.positions.insert(0, new_head)
            self.length += 1
            self.score += 10
        # Check if the new position of the snake's head is equal to the position of its body
        elif new_head in self.positions[1:]:
            # If yes, start over by resetting the snake's head and body
            self.reset()
        else:
            # If no, move the snake by adding the new head to the body and removing the tail
            self.positions.insert(0, new_head)
            if len(self.positions) > self.length:
                self.positions.pop()
