class Snake:
    def reset():
        global length, snake_head, score, food_position
        
        length = 1
        snake_head = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        score = 0
        food_position = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))