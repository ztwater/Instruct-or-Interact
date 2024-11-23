class ImageProcessor:
    def resize_image(image):
        if image.mode == 'RGB':
            width, height = image.size
            if width > 1000 or height > 1000:
                image = image.resize((width // 2, height // 2))
        return image