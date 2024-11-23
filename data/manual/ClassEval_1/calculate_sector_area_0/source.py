class AreaCalculator:
    def calculate_sector_area(self, angle):
        area = (angle / 360) * math.pi * (self.radius ** 2)
        return area