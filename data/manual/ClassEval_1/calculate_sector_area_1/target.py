class AreaCalculator:
    def calculate_sector_area(self, angle):
        """
        calculate the area of sector based on self.radius and angle
        :param angle: angle of sector, float
        :return: area of sector, float
        """
        area = (angle / 360) * math.pi * (self.radius ** 2)
        return area
