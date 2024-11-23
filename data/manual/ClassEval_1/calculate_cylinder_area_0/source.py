class AreaCalculator:
    def calculate_cylinder_area(self):
        base_area = 3.14159 * (self.radius ** 2)
        lateral_area = 2 * 3.14159 * self.radius * self.height
        total_area = 2 * base_area + lateral_area
        return total_area