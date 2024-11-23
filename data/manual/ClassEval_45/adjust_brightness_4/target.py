class ImageProcessor:
    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        """
        if self.image.mode in ('RGBA', 'LA'):
            # Convert image to RGB mode if it has an alpha channel or is in grayscale mode
            self.image = self.image.convert('RGB')

        enhancer = ImageEnhance.Brightness(self.image)
        adjusted_image = enhancer.enhance(factor)  # Adjust brightness by the given factor

        return adjusted_image