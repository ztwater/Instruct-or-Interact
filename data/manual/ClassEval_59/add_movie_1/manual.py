### Method Description:
    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """

### Solution Code:
    def add_movie(self, name, price, start_time, end_time, n):
        movie = {
            'name': name,
            'price': price,
            'start_time': datetime.strptime(start_time, '%H:%M'),
            'end_time': datetime.strptime(end_time, '%H:%M'),
            'seats': np.zeros((n, n))
        }
        self.movies.append(movie)

### Source Code:
    def add_movie(self, movie):
        self.movies.append(movie)

### Predicted Code:
    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        seats = np.zeros((n, n))
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        movie = {
            'name': name,
            'price': price,
            'start_time': datetime(1900, 1, 1, start_time.hour, start_time.minute),
            'end_time': datetime(1900, 1, 1, end_time.hour, end_time.minute),
            'seats': seats
        }
        self.movies.append(movie)


### Adaptation:
Total number: 13
### Raw Output:
```python
from datetime import datetime
import numpy as np

class MovieBookingSystem:  
    """
    this is a class as movie booking system, which allows to add movies, book tickets and check the available movies within a given time range. 
    """

    def __init__(self):
        """
        Initialize movies contains the information about movies
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        seats = np.zeros((n, n))
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        movie = {
            'name': name,
            'price': price,
            'start_time': datetime(1900, 1, 1, start_time.hour, start_time.minute),
            'end_time': datetime(1900, 1, 1, end_time.hour, end_time.minute),
            'seats': seats
        }
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        pass

    def available_movies(self, start_time, end_time):
        pass
```

### Test Code:
class MovieBookingSystemTestAddMovie(unittest.TestCase):
    def setUp(self):
        self.system = MovieBookingSystem()

    def tearDown(self):
        self.system = None

    def test_add_movie_1(self):
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 1)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[0]['price'], 49.9)
        self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
        self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
        self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))

    def test_add_movie_2(self):
        self.system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        self.system.add_movie('Superman', 49.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 2)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[1]['name'], 'Superman')

    def test_add_movie_3(self):
        self.system.add_movie('Batman', 39.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 1)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[0]['price'], 39.9)
        self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
        self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
        self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))

    def test_add_movie_4(self):
        self.system.add_movie('Batman', 29.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 1)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[0]['price'], 29.9)
        self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
        self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
        self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))

    def test_add_movie_5(self):
        self.system.add_movie('Batman', 19.9, '17:05', '19:25', 3)
        self.assertEqual(len(self.system.movies), 1)
        self.assertEqual(self.system.movies[0]['name'], 'Batman')
        self.assertEqual(self.system.movies[0]['price'], 19.9)
        self.assertEqual(self.system.movies[0]['start_time'], datetime.strptime('17:05', '%H:%M'))
        self.assertEqual(self.system.movies[0]['end_time'], datetime.strptime('19:25', '%H:%M'))
        self.assertEqual(self.system.movies[0]['seats'].shape, (3, 3))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: datetime
# field_dependencies: self.movies
# method_dependencies: 


