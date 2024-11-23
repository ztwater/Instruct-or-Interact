class ImageProcessor:
    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image.mode == 'RGB':
            width, height = self.image.size
            if width > 1000 or height > 1000:
                self.image = self.image.resize((width // 2, height // 2))
        return self.image