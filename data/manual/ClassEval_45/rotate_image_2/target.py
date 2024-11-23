class ImageProcessor:
    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(90)
        """
        if self.image:
            if self.image.mode == 'RGB':
                self.image = self.image.rotate(degrees)
            else:
                return "Image is not in RGB mode, cannot rotate."
        else:
            return "No image loaded."