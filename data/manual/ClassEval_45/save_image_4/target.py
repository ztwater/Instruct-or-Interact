class ImageProcessor:
    def save_image(self, save_path):
        if self.image is not None:
            self.image.save(save_path)
            print("Image saved successfully!")
        else:
            print("No image has been opened.")