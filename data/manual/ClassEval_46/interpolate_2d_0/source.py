class Interpolation:
    def interpolate_2d(data, x, y):
        """
        Interpolates a value in a 2D grid using bilinear interpolation.
        
        Args:
            data (list): A 2D grid of values.
            x (float): The x-coordinate of the point to interpolate.
            y (float): The y-coordinate of the point to interpolate.
        
        Returns:
            float: The interpolated value at the given coordinates.
        """
        x0 = int(x)
        y0 = int(y)
        x1 = x0 + 1
        y1 = y0 + 1
        
        q11 = data[y0][x0]
        q12 = data[y1][x0]
        q21 = data[y0][x1]
        q22 = data[y1][x1]
        
        x_diff = x - x0
        y_diff = y - y0
        
        interpolated_value = (1 - x_diff) * (1 - y_diff) * q11 + (1 - x_diff) * y_diff * q12 + x_diff * (1 - y_diff) * q21 + x_diff * y_diff * q22
        
        return interpolated_value