class ImageProcessor:
    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image is not None:
            if self.image.mode == 'RGB':
                image = self.image.resize((width, height))
                self.image = image
                return image
        return None