class AreaCalculator:
    def calculate_sphere_area(self):
        """
        calculate the area of sphere based on self.radius
        :return: area of sphere, float
        """
        return 4 * math.pi * (self.radius ** 2)