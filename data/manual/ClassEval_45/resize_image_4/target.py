class ImageProcessor:
    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        :return: None
        """

        if self.image.mode == 'RGB':
            self.image = self.image.resize((width, height))