class ImageProcessor:
    def rotate_image(self, degrees):
        """
        Rotate the image if it has been loaded
        :param degrees: float, the degrees that the image will be rotated
        """
        if self.image is None:
            return "No image has been loaded."
    
        if self.image.mode == 'RGB':
            self.image = self.image.rotate(degrees)
            return "Image rotated successfully."
        else:
            return "Image is not in RGB mode, cannot rotate."