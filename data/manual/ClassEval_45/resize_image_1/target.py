class ImageProcessor:
    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image is not None:
            if self.image.mode == 'RGB':
                image_width, image_height = self.image.size
                if image_width > 1000 or image_height > 1000:
                    self.image = self.image.resize((width // 2, height // 2))