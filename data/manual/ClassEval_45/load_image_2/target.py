class ImageProcessor:
    def load_image(self, image_path):
        """
        Use Image util in PIL to open an image
        :param image_path: str, path of the image that is to be loaded
        """
        self.image_path = image_path
        self.image = Image.open(self.image_path)