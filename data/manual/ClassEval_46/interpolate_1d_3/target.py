class Interpolation:
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :return: The y-coordinate of the interpolation point, list.
        """
        # Check if the input arrays have the same length
        if len(x) != len(y):
            raise ValueError("x and y must have the same length")

        # Initialize the output array
        y_interp = []

        # Perform linear interpolation for each x_interp value
        for x_val in x_interp:
            # Find the indices of the two closest x-coordinates in the original data
            idx = (np.abs(x - x_val)).argmin()

            # Perform linear interpolation using the two closest data points
            x1, x2 = x[idx], x[idx + 1]
            y1, y2 = y[idx], y[idx + 1]
            y_val = y1 + (y2 - y1) * (x_val - x1) / (x2 - x1)

            # Append the interpolated value to the output array
            y_interp.append(y_val)

        return y_interp
