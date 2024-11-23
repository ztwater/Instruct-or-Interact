class Snake:
    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        """
        snake_head = self.positions[-1]
        snake_body = self.positions[:-1]

        # Calculate the new position of the snake's head based on the direction
        if direction == "up":
            new_head = (snake_head[0], snake_head[1] - 1)
        elif direction == "down":
            new_head = (snake_head[0], snake_head[1] + 1)
        elif direction == "left":
            new_head = (snake_head[0] - 1, snake_head[1])
        elif direction == "right":
            new_head = (snake_head[0] + 1, snake_head[1])

        # Check if the new position of the snake's head is equal to the position of the food
        if new_head == self.food_position:
            # If yes, eat the food and increase the length of the snake by one
            snake_body.append(snake_head)
            snake_head = new_head
        # Check if the new position of the snake's head is equal to the position of its body
        elif new_head in snake_body:
            # If yes, start over by resetting the snake's head and body
            snake_head = (0, 0)
            snake_body = []
        else:
            # If no, move the snake by adding the new head to the body and removing the tail
            snake_body.append(snake_head)
            snake_head = new_head
            if len(snake_body) > self.length:
                snake_body.pop(0)

        self.positions = snake_body + [snake_head]