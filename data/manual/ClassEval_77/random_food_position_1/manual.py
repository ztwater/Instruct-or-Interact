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
        snake_positions = set(self.positions)
        while True:
            food_position = (random.randint(0, self.SCREEN_WIDTH-1), random.randint(0, self.SCREEN_HEIGHT-1))
            if food_position not in snake_positions:
                self.food_position = food_position
                break


### Adaptation:
Total number: 18
### Raw Output:
```
import random

class Snake:  
    """
    The class is a snake game, with allows snake to move and eat food, and also enables to reset, and generat a random food position.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        """
        Initialize the length of the snake, screen width, screen height, block size, snake head position, score, and food position.
        :param SCREEN_WIDTH: int
        :param SCREEN_HEIGHT: int
        :param BLOCK_SIZE: int, Size of moving units
        :param food_position: tuple, representing the position(x, y) of food.
        """
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.score = 0
        self.food_position = food_position

    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        snake_positions = set(self.positions)
        while True:
            food_position = (random.randint(0, self.SCREEN_WIDTH-1), random.randint(0, self.SCREEN_HEIGHT-1))
            if food_position not in snake_positions:
                self.food_position = food_position
                break

    def move(self, direction):
        pass

    def reset(self):
        pass

    def eat_food(self):
        pass
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


