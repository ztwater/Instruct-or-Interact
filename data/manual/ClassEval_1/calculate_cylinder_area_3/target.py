class AreaCalculator:
    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        """
        base_area = math.pi * (self.radius ** 2)
        lateral_area = 2 * math.pi * self.radius * height
        total_area = 2 * base_area + lateral_area
        return total_area