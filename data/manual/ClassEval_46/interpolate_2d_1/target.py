class Interpolation:
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        """
        interpolated_values = []
        
        for i in range(len(x_interp)):
            x0 = int(x_interp[i])
            y0 = int(y_interp[i])
            x1 = x0 + 1
            y1 = y0 + 1
            
            q11 = z[y0][x0]
            q12 = z[y1][x0]
            q21 = z[y0][x1]
            q22 = z[y1][x1]
            
            x_diff = x_interp[i] - x0
            y_diff = y_interp[i] - y0
            
            interpolated_value = (1 - x_diff) * (1 - y_diff) * q11 + (1 - x_diff) * y_diff * q12 + x_diff * (1 - y_diff) * q21 + x_diff * y_diff * q22
            interpolated_values.append(interpolated_value)
        
        return interpolated_values