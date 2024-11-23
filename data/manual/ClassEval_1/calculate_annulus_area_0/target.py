class AreaCalculator:
    def calculate_annulus_area(self, inner_radius, outer_radius):
        """
        calculate the area of annulus based on inner_radius and out_radius
        :param inner_radius: inner radius of sector, float
        :param outer_radius: outer radius of sector, float
        :return: area of annulus, float
        >>> areaCalculator.calculate_annulus_area(2, 3)
        15.707963267948966
        """
        if inner_radius >= outer_radius:
            return "Error: Inner radius must be smaller than outer radius."
        else:
            annulus_area = math.pi * (outer_radius**2 - inner_radius**2)
            return annulus_area

