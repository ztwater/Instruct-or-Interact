class AreaCalculator:
    def calculate_sphere_area(self):
        """
        Calculate the area of a sphere based on the radius.
        :return: area of sphere, float
        """
        return 4 * math.pi * (self.radius ** 2)