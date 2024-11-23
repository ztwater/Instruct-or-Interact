class ImageProcessor:
    def load_image(self, image_path):
        self.image = Image.open(image_path)