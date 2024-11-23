class ImageProcessor:
    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
        if self.image is not None:
            self.image.save(save_path)
            print("Image saved successfully!")
        else:
            print("No image has been opened.")