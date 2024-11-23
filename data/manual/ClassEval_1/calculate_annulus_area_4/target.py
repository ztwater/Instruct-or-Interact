class AreaCalculator:
    def calculate_annulus_area(self, inner_radius, outer_radius):
        if inner_radius >= outer_radius:
            return "Error: Inner radius must be smaller than outer radius."
        else:
            annulus_area = math.pi * (outer_radius**2 - inner_radius**2)
            return annulus_area