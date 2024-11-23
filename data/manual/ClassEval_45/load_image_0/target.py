class ImageProcessor:
    def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        :param image_path: str, path of image that is to be
        """
        self.image = Image.open(image_path)