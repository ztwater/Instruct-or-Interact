class ImageProcessor:
    def rotate_image(self, degrees):
        """
        Rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        """
        if self.image is None:
            return "No image loaded."
        
        if self.image.mode == 'RGB':
            self.image = self.image.rotate(degrees)
        else:
            return "Image is not in RGB mode, cannot rotate."