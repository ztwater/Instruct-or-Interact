class Snake:
    def eat_food(snake, food, score):
        # Increase the length of the snake by 1
        snake.append(snake[-1])
        
        # Increase the score by 100
        score += 100
        
        # Randomly generate a new food position
        food = (random.randint(0, 9), random.randint(0, 9))
        
        return snake, food, score