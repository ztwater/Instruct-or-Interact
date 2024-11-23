### Method Description:
    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """

### Solution Code:
    def random_food_position(self):
        while self.food_position in self.positions:
            self.food_position = (random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE,
                                  random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE)

### Source Code:
    def random_food_position(snake_positions, grid_size):
        while True:
            food_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
            if food_position not in snake_positions:
                return food_position

### Predicted Code:
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

### Adaptation:
Total number: 17
### Raw Output:
```
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
```

### Test Code:
class SnakeTestRandomFoodPosition(unittest.TestCase):
    def test_random_food_position_1(self):
        snake = Snake(100, 100, 1, (51, 51))
        self.assertEqual(snake.food_position, (51, 51))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

    def test_random_food_position_2(self):
        snake = Snake(100, 100, 1, (99, 99))
        self.assertEqual(snake.food_position, (99, 99))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

    def test_random_food_position_3(self):
        snake = Snake(100, 100, 1, (0, 0))
        self.assertEqual(snake.food_position, (0, 0))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

    def test_random_food_position_4(self):
        snake = Snake(100, 100, 1, (40, 40))
        self.assertEqual(snake.food_position, (40, 40))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

    def test_random_food_position_5(self):
        snake = Snake(100, 100, 1, (60, 60))
        self.assertEqual(snake.food_position, (60, 60))
        snake.random_food_position()
        self.assertNotIn(snake.food_position, snake.positions)
        self.assertGreaterEqual(snake.food_position[0], 0)
        self.assertGreaterEqual(snake.food_position[1], 0)
        self.assertLessEqual(snake.food_position[0], 100)
        self.assertLessEqual(snake.food_position[1], 100)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: random
# field_dependencies: self.BLOCK_SIZE, self.SCREEN_HEIGHT, self.SCREEN_WIDTH, self.food_position, self.positions
# method_dependencies: 


