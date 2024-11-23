class Snake:
    def move(direction, snake_head, snake_body, food_position):
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
        if new_head == food_position:
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
            if len(snake_body) > snake_length:
                snake_body.pop(0)
    
        return snake_head, snake_body