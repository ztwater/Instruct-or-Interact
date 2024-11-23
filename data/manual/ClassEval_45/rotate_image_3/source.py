class ImageProcessor:
    def rotate_image(image):
        if image.mode == 'RGB':
            image = image.rotate(90)
            return image
        else:
            return "Image is not in RGB mode, cannot rotate."