class ImageProcessor:
    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        """
        if self.image is not None:
            image = self.image.copy()

            if image.mode in ('RGBA', 'LA'):
                # Convert image to RGB mode if it has an alpha channel or is in grayscale mode
                image = image.convert('RGB')

            enhancer = ImageEnhance.Brightness(image)
            adjusted_image = enhancer.enhance(factor)

            self.image = adjusted_image
        else:
            raise ValueError("Please load an image before adjusting the brightness.")
