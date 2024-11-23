class AreaCalculator:
    def calculate_cylinder_area(self, height):
        """
        calculate the area of cylinder based on self.radius and height
        :param height: height of cylinder, float
        :return: area of cylinder, float
        >>> areaCalculator = AreaCalculator(2)
        >>> areaCalculator.calculate_cylinder_area(3)
        62.83185307179586
        """
        base_area = math.pi * (self.radius ** 2)
        lateral_area = 2 * math.pi * self.radius * height
        total_area = 2 * base_area + lateral_area
        return total_area